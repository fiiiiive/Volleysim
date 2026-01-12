# Volleysim

Volleysim is a small, text-based volleyball simulation game written in Python. I built it mostly out of boredom and curiosity — I wanted something simple but entertaining that could simulate full volleyball seasons without any graphics or user input beyond running the program.

The simulator models three leagues (League A, League B, and League C), each with its own rules for season length, playoffs, and promotion or relegation. Teams move up and down between leagues based on their performance, which makes each season feel a little different.

Matches are simulated point-by-point using a stat-driven system. Each team has offensive and defensive attributes (serve, swing, block, and defense), and for every point a random stat is selected and compared between teams. The higher value wins the point, and matches follow standard volleyball rules with best-of-three sets (and shorter final sets).

This project isn’t meant to be realistic or competitive — it’s just a fun programming sandbox where I could build a small game, experiment with simulation logic, and watch leagues evolve over time. 
