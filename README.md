# evi-rescue-robot
Evi is an autonomous rescue robot using SLAM and AMCL for real-time navigation in disaster zones. Built with ROS, Raspberry Pi, and Teensy 3.2, it performs mapping and obstacle avoidance with high accuracy using LIDAR, IR sensors, and PID motor control.


# 🤖 Evi – The Rescue Assisting Robot

An autonomous mobile robot designed to navigate in disaster-affected environments using SLAM and AMCL techniques for rescue assistance. Built with ROS and sensor integration to map, localise, and avoid obstacles in real-time.

📄 [View Full Report](docs/REPORT.pdf) <!-- Replace with actual file if available -->

---

## 🧭 System Architecture

![Evi Architecture](docs/images) <!-- Replace with actual image -->

---

## ⚙️ Technologies Used

- **Localization**: AMCL (Adaptive Monte Carlo Localization)
- **Mapping**: SLAM (Simultaneous Localisation and Mapping)
- **Simulation**: ROS + RViz
- **Hardware**: Custom-built chassis with differential drive
- **Sensors**: IR sensors, Ultrasonic, Lidar
- **Programming**: Python, C++
- **Microcontrollers**: Raspberry Pi + Arduino

---

## 🧩 Core Features

✅ Real-time environment mapping using SLAM  
✅ AMCL-based localisation for precise path execution  
✅ Obstacle detection and avoidance using sensor fusion  
✅ Autonomous path planning to navigate cluttered terrain  
✅ Real-time visual feedback in RViz  
✅ Modular hardware platform for rugged disaster zones

---

## 🎥 Demo & Results

<!-- Replace this with real video link -->
[![Watch Demo](https://www.linkedin.com/posts/gowtham-sridher_well-final-output-of-slam-and-navigation-activity-6680736161427689472-7Em7?utm_source=linkedin_share&utm_medium=member_desktop_web&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_projects_details%3BOLeADoH9SwWy%2FvnBWcQHbA%3D%3D)

---

## 📚 Learnings

- Sensor data fusion and tuning
- Navigation stack setup in ROS
- Integration between Raspberry Pi and Arduino over serial
- Calibration of Lidar with robot base frame
- Working with ROS topics and transform trees (TF)

---

## 📂 Suggested Folder Structure

```bash
evi-rescue-robot/
├── docs/
│   ├── EVI_REPORT.pdf
│   └── images/
│       ├── evi-architecture.png
│       └── rviz-mapping.png
├── src/
├── launch/
├── urdf/
├── scripts/
├── README.md
