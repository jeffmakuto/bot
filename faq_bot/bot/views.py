from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .bot_manager import RuleBasedBot, Admin
from .smtp_config import SMTPConfig

# Initialize instances
bot_instance = RuleBasedBot()
admin_instance = Admin(bot_instance)

smtp_config_instance = SMTPConfig(
    smtp_server='',
    smtp_port=587,
    sender_email='',
    sender_password='',
    recipient_email=''
)

@csrf_exempt
def bot_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('user_input')
            if user_input is None:
                return JsonResponse({'error': 'User input is required'}, status=400)

            bot_response = bot_instance.respond(
                user_input,
                admin_instance,
                smtp_config_instance.smtp_server,
                smtp_config_instance.smtp_port,
                smtp_config_instance.sender_email,
                smtp_config_instance.sender_password,
                smtp_config_instance.recipient_email
            )

            return JsonResponse({'bot_response': bot_response})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Only POST requests are allowed.'}, status=400)
