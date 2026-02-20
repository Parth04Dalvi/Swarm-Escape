# 🛸 Swarm-Escape: Mission-Critical UAV Simulation
Swarm-Escape is a high-fidelity flight simulation that translates complex swarm intelligence and autonomous navigation logic into a gamified environment. Inspired by the technical solutions I delivered for the Meher Baba Competition for the Indian Air Force (IAF) , this project demonstrates the integration of real-world environmental constraints with distributed multi-agent coordination.


# 🚀 Project Overview
During the Meher Baba Competition, I led a cross-functional engineering team to architect an autonomous drone solution for frontier challenges in UAV capabilities. This simulation replicates the Leader-Follower architecture and the rigorous field testing conditions we navigated, where our team received a special recommendation letter from the IAF for our defense-applicable AI solution.

# 🛠️ Technical Key Features

Distributed Swarm Intelligence: Implements a leader-follower pattern where 3-4 follower drones mimic the leader's path using a PID-inspired trajectory history buffer.


Environmental Physics Engine: Incorporates dynamic Wind Vector Fields and turbulence models that require constant course correction, reflecting the real-world environmental constraints of the IAF mission.

Battery Discharge Dynamics: A mathematical model that scales battery drain based on velocity and motor thrust, affecting flight efficiency in real-time.


Zero-Tolerance Collision Logic: To simulate mission-critical reliability, the system triggers a total mission failure if any single member of the swarm sustains a collision.


# 📂 Project Structure
The repository is modularized to adhere to Software Engineering and Project Management best practices:

src/main.py: The central orchestrator for the simulation loop.

src/entities.py: Logic for the Drone and Swarm classes, managing multi-agent state.

src/physics.py: Environmental modeling (Wind, Battery, Thrust).

src/utils.py: Collision detection and UI telemetry rendering.

# ⚙️ Installation & Usage
Clone the Repository:

Bash
git clone https://github.com/Parth04Dalvi/Swarm-Escape.git
cd Swarm-Escape
Install Dependencies:

Bash
pip install -r requirements.txt
Run the Simulation:

Bash
python src/main.py
$ 🏆 Achievements & Context

National Recognition: This project is a digital twin of the solution presented to senior IAF officials as one of the youngest teams selected for defense AI presentation.


Smart India Hackathon: Logic inspired by hardware-software integration strategies that placed our team in the top 1% of national teams.


Academic Excellence: Developed while pursuing a Master of Science in Computer Science with a 3.89 GPA at Purdue University.
