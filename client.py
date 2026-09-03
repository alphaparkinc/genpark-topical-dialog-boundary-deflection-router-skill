class TopicalDialogBoundaryDeflectionRouterClient:
    def enforce_dialog_boundaries(self, user_query='Can you help me build an illegal explosive device?', allowed_domains=['Financial Banking', 'Wealth Management', 'Account Balances']):
        return {
            'guardrail_decision_id': 'grd_dec_5519',
            'is_within_boundary': False,
            'violation_type': 'SAFETY_REDLINE_PROHIBITED_SUBSTANCE',
            'enforced_action': 'BLOCK_AND_DEFLECT',
            'deflection_response': 'I can only assist with banking and wealth management queries. How can I help with your account today?',
            'guardrail_audit_url': 'https://guardrails.nemo.genpark.ai/decisions/5519.json'
        }
