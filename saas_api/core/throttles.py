from rest_framework.throttling import UserRateThrottle

from .models import UserPlan


class PlanBasedThrottle(UserRateThrottle):

    scope = 'plan_based'

    def get_rate(self):

        user = self.request.user

        if not user.is_authenticated:
            return '3/min'

        try:
            user_plan = UserPlan.objects.get(user=user)

            if user_plan.plan == 'premium':
                return '20/min'

            return '5/min'

        except UserPlan.DoesNotExist:
            return '5/min'