from urllib.request import Request, urlopen
from urllib.parse import urlparse
from html import unescape
import re

from tools.evidence_store import save_evidence


def fetch_webpage(url: str) -> dict:
    """Fetch a public webpage and persist successful research evidence."""

    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        return {
            "success": False,
            "url": url,
            "error": "Only HTTP and HTTPS URLs are allowed."
        }

    try:
        request = Request(
            url,
            headers={
                "User-Agent": "LIFEOPS Research Agent/1.0"
            }
        )

        with urlopen(request, timeout=15) as response:
            raw = response.read().decode("utf-8", errors="replace")

        text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S | re.I)
        text = re.sub(r"<style.*?</style>", " ", text, flags=re.S | re.I)
        text = re.sub(r"<[^>]+>", " ", text)
        text = unescape(text)
        text = re.sub(r"\s+", " ", text).strip()

        excerpt = ""

        for needle in (
            "example.com",
            "reserved",
            "Section 3",
            "section 3"
        ):
            index = text.lower().find(needle.lower())

            if index != -1:
                start = max(0, index - 500)
                end = min(len(text), index + 1200)
                excerpt = text[start:end]
                break

        if not excerpt:
            excerpt = text[:1500]

        evidence = save_evidence(
            url=url,
            domain=parsed.netloc,
            text=text[:20000],
            excerpt=excerpt
        )

        return {
            "success": True,
            "url": url,
            "domain": parsed.netloc,
            "text": text[:20000],
            "excerpt": excerpt,
            "evidence_id": evidence["id"]
        }

    except Exception as exc:
        return {
            "success": False,
            "url": url,
            "error": str(exc)
        }
