from simple_sso.sso_server.models import Token


def logout_token(sender, request, **kwargs):
    """
    A signal receiver which removes a token when its users logs out.
    """
    tokens = Token.objects.select_related("session").filter(
        session__session_key=request.session.session_key
    )

    for token in tokens:
        token.delete()
