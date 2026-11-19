# Craft: charts and data

Rules below are established practice (Tufte, Cairo, Knaflic). The research notes mark them as stated from memory, so treat them as craft guidance, not as findings.

## Read the data first

- Check axes, units, date range and which column is which before describing a trend.
- Recompute the headline number from the rows. Run it in code when you can.
- Look for missing values, mixed units and changed definitions.
- State what the data cannot show.

## Pick the chart from the question

| Question | Chart |
|---|---|
| Compare amounts | Bar, zero baseline |
| Change over time | Line; endpoints labelled |
| Part of a whole, few parts | Bar or labelled segments |
| Relationship of two measures | Scatter |
| Exact lookup | Table |

Skip 3D effects and pies with many slices.

## Axes

- Bars start at zero. A bar chart that starts at 95 exaggerates.
- Lines may start off zero. Show the baseline and say the change in words.
- Use one date range across comparisons. If it differs, say why.
- Avoid dual axes with unrelated scales.
- Do not choose a start date to make a trend look steeper.

## Colour and ink

- Grey for context, one saturated colour for the point.
- Label series directly at the line end instead of a distant legend.
- Remove borders and heavy gridlines. Keep one baseline.
- Do not use rainbow colour for categories that have no order.
- Check it still reads in greyscale and for colour-blind readers.

## Titles and notes

- Slide or report title: the takeaway. Chart title or subtitle: what is plotted, with unit.
- Under every chart: source, date, unit, n, and any metric definition that is not obvious.
- Annotate the one thing to notice.

## Describing a chart in text

- Say what is plotted, then the finding, then the size ("fell from X to Y between A and B").
- Do not call it "significant" without a test. Say "large" with the numbers.
- Correlation is not cause. Say it once.

## Spreadsheet-backed charts

- Keep every driver once, labelled with unit and source. Formulas point to it. No pasted constants in calculation cells.
- Check that totals sum and periods match.
- The FAST Standard (edition 02c, July 2019) is the professional reference for modelling structure. The version may be out of date.

## Longer before and after

**Before:** A line chart of monthly sign-ups, y-axis from 9,800 to 10,400, a rainbow of six lines, legend at the right, no unit. Caption: "Sign-ups are surging."

**After:** Axis from 0, or a labelled baseline if kept off zero. One accent line for the product in question, five grey lines. Series labelled at their ends. Title: "Sign-ups rose [x]% between [month] and [month]". Subtitle: "Monthly new accounts, [region]. Source: [system], [date]."

The after chart does not exaggerate the change, and a reader can tell what is plotted, from where and when. The figures are placeholders; fill them from the dataset.
