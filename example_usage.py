from client import TopicalDialogBoundaryDeflectionRouterClient

def main():
    client = TopicalDialogBoundaryDeflectionRouterClient()
    res = client.enforce_dialog_boundaries('What is my portfolio balance?')
    print('Dialog Boundary Deflection Router: ' + res['guardrail_decision_id'])
    print('Within Boundary: ' + str(res['is_within_boundary']) + ' | Action: ' + res['enforced_action'])
    print('Audit URL: ' + res['guardrail_audit_url'])

if __name__ == '__main__':
    main()
