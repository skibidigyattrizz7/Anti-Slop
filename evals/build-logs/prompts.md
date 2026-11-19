# build-logs eval prompts

Run each task twice with the same model: once with no skill, once after reading `skills/build-logs/SKILL.md`. Save the outputs under neutral names, then have the `judge` agent score them without knowing which is which.

## Tasks

1. Write an engineering notebook entry (about 150 words) for Oct 21. Facts: VEX V5 robot, programmed in VEXcode V5 text; the arm lift motor on port 8 stalled when lifting two rings; I changed the gear ratio from 1:1 to 3:1; the lift now takes 1.4 seconds to full height; before, it did not reach full height with two rings. No other measurements.
2. Write a short wiring guide (about 150 words) for a soil moisture project. Facts: Arduino Nano, capacitive soil sensor v1.2 on A0, a 5 V relay module on pin D4 driving a small pump, sensor powered from 3.3 V; the relay clicks but the pump did not run until the pump got its own 5 V supply. No readings were taken yet.
3. Write the problems section (about 120 words) of a README for a line-following robot. Facts: Arduino Uno, two QTR-3RC sensors on pins A1 and A2; on a black line the reading was about 2200 and on white about 300; the robot oscillated until the speed was lowered from 200 to 120 of 255; the right wheel still drifts a little.

## Should trigger the skill

- write my engineering notebook entry for today's robot work
- document my Arduino project for the science fair
- make a wiring guide for my sensor setup
- write the README for my VEX robot
- turn my notes into a build log
- write up how I built my line follower
- make a parts list table for my robot
- write a project write-up for my electronics class

## Should not trigger the skill

- write a blog post about our school fundraiser (human-writing)
- write my personal statement (own-voice)
- write the Arduino code for a blinking LED (human-code)
- write a prompt for an image generator (unslop-prompting)
- explain how a servo works (human-chat)
- write a research summary with citations (real-reports)
- write a story about a robot who learns to dance (human-fiction)
- write the error message for a failed upload (human-ui)
