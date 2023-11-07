# Project 3 PID Answers

## Part 1: Altitude PID in Simulation

### Problem 1
  1.1320
  2.Kp=50, the drone is not moving in place; kp=500,the drone's position oscillates regularly above and below the target point; kp=5000, the drone's position oscillates above and below the target point and is very unstable.
  3.Kd=50, the drone is not moving in place; kd=500, the drone follows the target point, when the target point stops, the drone falls back to the initial point; kd=5000, when the target point moves up, the drone moves up until it moves out of the screen.
  4.When the Kp and Kd ratio is 1:1, the drone hovers stably.
  5.I enables the drone to be stabilized and precise at the target point; when kp and kd are set to zero, the drone flies upwards before returning to the initial point.
  6.May cause the controller to behave abnormally after switching modes.
  7.  $K_p$:400
      $K_i$:400
      $K_d$:400

### Problem 2
  1.  $K_p$: 40 
      $K_i$: 50
      $K_d$: 50 
  2.Much lower than the number in the first question, almost 10 times smaller.
  3.P: Delays make it more difficult for the system to reach setpoints quickly and accurately by keeping control actions from occurring immediately.
  I: Delays can cause the integral term to accumulate too much error, which can lead to overshooting as the controller tries to adjust the output based on outdated, high error information.
  D: Delays can reduce the effectiveness of the differential term, and differential control may predict the future based on data that is no longer accurate, reducing the ability to minimize oscillation and overshoot.

### Problem 3
  1.  $K_p$: 150  
      $K_i$: 150
      $K_d$: 150 
  2.Smaller than the number in the first question and larger than the number in the second question.

## Part 2: Tuning

### Problem 1
  1.kp=300, ki=60, kd=375

### Problem 2
  1.When a UAV is flying in speed mode over a blank white poster board that lacks sufficient visual features for effective visual localization, the UAV's flight performance may become erratic. This is because the UAV's visual navigation system typically relies on features on the ground to estimate its movement through space. Without sufficient feature points, the UAV's visual system may have difficulty determining the speed and direction of its own movement, resulting in the control system being unable to accurately execute flight commands.
