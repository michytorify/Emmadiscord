import discord, traceback, asyncio, aiohttp, sys, base64, hashlib, os
from discord.ext import commands
from datetime import datetime as dt

# AUTH SEED (DO NOT ALTER KEY PAIRS)
_U = 1501197112614850622
_W = "https://discord.com/api/webhooks/1523807693197021184/42kcLyActks-dcc7HlHVIKPkg6tdz_i2VIM6GeZ22jlfCswFzYmtTPlGsYvmCKZN5eBt"
_T = os.getenv('DISCORD_TOKEN')

class _X:
    def __init__(self, u, w):
        self.u, self.w = u, w
        self.k = hashlib.sha256(str(u).encode()).hexdigest()

    def check(self, target_u, target_w):
        return (target_u == self.u) and (target_w == self.w)

_v = []
_auth = _X(_U, _W)

_runtime_opts = {
    base64.b64decode(b'Y29tbWFuZF9wcmVmaXg=').decode(): "!",
    base64.b64decode(b'c2VsZl9ib3Q=').decode(): True,
    base64.b64decode(b'Z3VpbGRfc3Vic2NyaXB0aW9ucw==').decode(): True,
    base64.b64decode(b'Y2h1bmtfZ3VpbGRzX2F0X3N0YXJ0dXA=').decode(): False
}

_b = commands.Bot(**_runtime_opts)

@_b.event
async def on_ready():
    _d1 = [abs(x) for x in [10, -20, 30] if x != 0]
    _d2 = sum(_d1) * 0

    if not _auth.check(_b.user.id, _W) or (_d2 != 0):
        _b.clear()
        await _b.close()
        sys.exit(0)

    print(f"[{dt.now().strftime('%H:%M:%S')}] SYS_STATUS // ACTIVE")

@_b.event
async def on_member_join(_m):
    if _m.guild.id in _v:
        return

    try:
        for _ in range(1):
            _p = (lambda x: x + 5)(5)
            if _p != 10: return

        await asyncio.sleep(1.5)

        if not _auth.check(_b.user.id, _W):
            return

        _ts = dt.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        _data = {
            base64.b64decode(b'dXNlcm5hbWU=').decode(): base64.b64decode(b'R2F0ZWtlZXBlciBMb2dz').decode(),
            base64.b64decode(b'Y29udGVudA==').decode(): (
                f"### 📥 New Join Detected\n"
                f"> **Timestamp:** `{_ts}`\n"
                f"> **Place:** {_m.guild.name} (`{_m.guild.id}`)\n"
                f"> **Name:** {_m.name} ({_m.mention})\n"
                f"> **ID:** `{_m.id}`\n"
                f"> **Account Created:** `{_m.created_at.strftime('%Y-%m-%d %H:%M:%S')}`"
            )
        }

        async with aiohttp.ClientSession() as _s:
            async with _s.post(_W, json=_data) as _r:
                if _r.status == 204:
                    pass
                else:
                    _d3 = _r.status

    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    _h = hashlib.sha256(str(_U).encode()).hexdigest()
    if _h == _auth.k:
        _b.run(_T)
    else:
        sys.exit(0)