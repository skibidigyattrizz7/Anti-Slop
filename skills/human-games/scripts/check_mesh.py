#!/usr/bin/env python3
"""Count facts about a Wavefront .obj mesh. Evidence for a reviewer, never a verdict.

Usage:
  python3 check_mesh.py [--max-tris N] FILE.obj          human-readable report
  python3 check_mesh.py [--max-tris N] --json FILE.obj   JSON report
  python3 check_mesh.py --selftest

Reports vertex, face and triangle counts, whether UVs and normals exist, and
degenerate faces (fewer than 3 corners, a repeated vertex, or zero area).
Flags: triangles above --max-tris (default 5000), no UVs, no normals, degenerate faces.
Exit codes: 0 no flags, 1 flags, 2 usage error.
"""
import json, sys

DEFAULT_MAX = 5000


def analyze(text, max_tris=DEFAULT_MAX):
    verts, vt, vn, faces = [], 0, 0, []
    for line in text.splitlines():
        p = line.split()
        if not p:
            continue
        if p[0] == "v" and len(p) >= 4:
            verts.append(tuple(float(x) for x in p[1:4]))
        elif p[0] == "vt":
            vt += 1
        elif p[0] == "vn":
            vn += 1
        elif p[0] == "f":
            faces.append(p[1:])
    tris = degenerate = 0
    for f in faces:
        idx = []
        for c in f:
            i = int(c.split("/")[0])
            idx.append(i - 1 if i > 0 else len(verts) + i)  # negative = relative
        tris += max(len(idx) - 2, 0)
        bad = len(idx) < 3 or len(set(idx)) < len(idx) or any(not 0 <= i < len(verts) for i in idx)
        if not bad:
            a, b, c = (verts[i] for i in idx[:3])
            u = [b[k] - a[k] for k in range(3)]
            w = [c[k] - a[k] for k in range(3)]
            cr = (u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0])
            bad = sum(x * x for x in cr) < 1e-18
        degenerate += bad
    r = {"vertices": len(verts), "faces": len(faces), "triangles": tris,
         "has_uvs": vt > 0, "has_normals": vn > 0, "degenerate_faces": degenerate,
         "max_tris": max_tris}
    flags = []
    if tris > max_tris: flags.append(f"{tris} triangles, above {max_tris}")
    if not r["has_uvs"]: flags.append("no UVs")
    if not r["has_normals"]: flags.append("no normals")
    if degenerate: flags.append(f"{degenerate} degenerate faces")
    r["flags"] = flags
    return r


def report(r):
    out = [f"{k}: {v}" for k, v in r.items() if k != "flags"]
    out.append("flags: " + ("; ".join(r["flags"]) if r["flags"] else "none"))
    out.append("Counts are evidence, not proof. Look at the model from the back and up close too.")
    return "\n".join(out)


def selftest():
    cube_quad = ("v 0 0 0\nv 1 0 0\nv 1 1 0\nv 0 1 0\nvt 0 0\nvn 0 0 1\nf 1/1/1 2/1/1 3/1/1 4/1/1\n")
    r = analyze(cube_quad)
    assert (r["vertices"], r["faces"], r["triangles"]) == (4, 1, 2), r
    assert r["has_uvs"] and r["has_normals"] and r["flags"] == [], r
    bad = "v 0 0 0\nv 1 0 0\nv 2 0 0\nf 1 2 3\nf 1 1 2\n"
    r = analyze(bad)
    assert r["degenerate_faces"] == 2 and not r["has_uvs"] and r["flags"], r
    assert analyze(cube_quad, max_tris=1)["flags"], "threshold"
    assert analyze("v 0 0 0\nv 1 0 0\nv 0 1 0\nf -3 -2 -1\n")["degenerate_faces"] == 0, "negative idx"
    print("selftest ok")


def main(argv):
    if argv == ["--selftest"]:
        selftest()
        return 0
    as_json, max_tris, paths = False, DEFAULT_MAX, []
    i = 0
    try:
        while i < len(argv):
            if argv[i] == "--json":
                as_json = True
            elif argv[i] == "--max-tris":
                i += 1
                max_tris = int(argv[i])
            else:
                paths.append(argv[i])
            i += 1
        if len(paths) != 1:
            raise ValueError
        text = open(paths[0], encoding="utf-8", errors="replace").read()
        r = analyze(text, max_tris)
    except (ValueError, IndexError, OSError):
        print(__doc__, file=sys.stderr)
        return 2
    print(json.dumps(r, indent=2) if as_json else report(r))
    return 1 if r["flags"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
