from __future__ import division


class PID:
    """
    This is your PID class! Be sure to read the docstrings carefully and fill in all methods of this class!
    """

    def __init__(self, kp, ki, kd, k):
        """
        Here is where you will initialize all of the instance variables you might need!

        **IMPORTANT** Be sure to follow the following naming conventions for your control term variables:

        P term: _p
        I term: _i
        D term: _d

        This will ensure that your class works correctly with the rest of the drone's code stack.

        :param kp: The proportional gain constant
        :param ki: The integral gain constant
        :param kd: The derivative gain constant
        :param k: The offset constant that will be added to the sum of the P, I, and D control terms
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.k = k

        # 初始化 P, I, D 控制项
        

        # 初始化额外的变量
        self._previous_error = 0
        self._cumulative_error = 0


    def step(self, err, dt):
        """
        This method will get called at each sensor update, and should return
        a throttle command output to control the altitude of the drone. This is where
        your actual PID calculations will occur. You should implement the discrete version
        of the PID control function.

        :param err: The current error (difference between the setpoint and drone's current altitude) in meters.
                    For example, if the drone was 10 cm below the setpoint, err would be 0.1
        :param dt: The time (in seconds) elapsed between measurements of the process variable (the drone's altitude)
        :returns: You should restrict your output to be between 1100 and 1900. This is a PWM command, which will be
                  sent to the SkyLine's throttle channel
        """
        # 更新 P, I, D 控制项
        #P
        self._p = self.kp * err
        #I
        self._cumulative_error += err * dt
        self._i = self.ki * self._cumulative_error
        if dt > 0:  # 防止除以零
            self._d = self.kd * ((err - self._previous_error) / dt)
        else:
            self._d = 0

        # 更新前一个误差值
        self._previous_error = err

        # 计算总输出
        output = self._p + self._i + self._d + self.k

        # 限制输出范围
        return max(1100, min(1900, output))

    def reset(self):
        """
        This method will get called when the simulation is reset (by pressing 'r') or when the real drone transitions
        from armed mode to flying mode. You will want to reset the PID terms so that previously stored values will
        not affect the current calculations (think about what this entails)!
        """
        # 重置积分项和微分项相关的内部变量
        self._cumulative_error = 0  # 重置累积误差
        self._previous_error = 0    # 重置上一次的误差

        # 也可以选择重置 P, I, D 控制项本身，如果需要的话
        self._p = 0
        self._i = 0
        self._d = 0
