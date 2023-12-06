
class LeaveApprovalExpertSystem:
    def __init__(self, leave_balance, team_workload):
        self.leave_balance = leave_balance
        self.team_workload = team_workload

    def process_leave_request(self, leave_duration):
        if leave_duration <= self.leave_balance:
            return "Leave Approved"
        elif leave_duration > self.leave_balance and leave_duration <= (self.leave_balance + 5):
            return "Leave Approved with Deduction"
        elif self.team_workload == "High":
            return "Leave Denied - High Workload"
        else:
            return "Leave Denied - Unknown Reason"

# Example Usage:
leave_system = LeaveApprovalExpertSystem(10, "Medium")

# Employee requests leave for 8 days
result = leave_system.process_leave_request(8)
print(result)

# Employee requests leave for 15 days
result = leave_system.process_leave_request(15)
print(result)

# Employee requests leave during a high workload period
leave_system.team_workload = "High"
result = leave_system.process_leave_request(5)
print(result)
