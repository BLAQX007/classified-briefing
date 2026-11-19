from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Classified Briefing")

# ==========================================
# CUSTOMIZE THESE TWO LINES FOR HER
HER_NAME = "Bianca"
YOUR_NAME = "Thato"
# ==========================================

@app.get("/", response_class=HTMLResponse)
def serve_date_site():
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>TOP SECRET // FOR {HER_NAME.upper()} ONLY</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: radial-gradient(circle at top, #1e1b4b 0%, #09090b 75%);
            color: #ffffff;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 16px;
            overflow-x: hidden;
            touch-action: manipulation;
        }}
        .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
        .container {{ width: 100%; max-width: 430px; }}
        .progress-header {{
            display: flex; justify-content: space-between;
            font-size: 11px; color: #a1a1aa; margin-bottom: 6px;
        }}
        .progress-track {{
            width: 100%; height: 6px; background: #27272a;
            border-radius: 99px; overflow: hidden; margin-bottom: 20px;
        }}
        .progress-fill {{
            height: 100%; width: 25%;
            background: linear-gradient(90deg, #f43f5e, #fbbf24);
            transition: width 0.4s ease;
        }}
        .card {{
            background: rgba(24, 24, 27, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 24px;
            padding: 28px 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
            min-height: 460px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: relative;
        }}
        .hidden {{ display: none !important; }}
        .fade-in {{ animation: fadeIn 0.45s ease forwards; }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(14px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .badge {{
            display: inline-block; font-size: 11px; font-weight: 700;
            padding: 5px 12px; border-radius: 99px; margin-bottom: 14px;
        }}
        .badge-rose {{ background: rgba(244, 63, 94, 0.15); color: #fda4af; border: 1px solid rgba(244, 63, 94, 0.35); }}
        .badge-amber {{ background: rgba(251, 191, 36, 0.15); color: #fcd34d; border: 1px solid rgba(251, 191, 36, 0.35); }}
        h1 {{ font-size: 28px; font-weight: 800; margin-bottom: 8px; }}
        h2 {{ font-size: 22px; font-weight: 800; margin-bottom: 6px; line-height: 1.25; }}
        .sub {{ font-size: 13px; color: #a1a1aa; line-height: 1.5; }}
        .center {{ text-align: center; }}

        /* Scanner */
        .scan-wrap {{ display: flex; flex-direction: column; align-items: center; margin: 26px 0; }}
        .scan-btn {{
            width: 112px; height: 112px; border-radius: 50%;
            background: #18181b; border: 2px solid #f43f5e;
            color: #fda4af; cursor: pointer;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            box-shadow: 0 0 28px rgba(244, 63, 94, 0.4);
            user-select: none; -webkit-user-select: none; -webkit-touch-callout: none;
            transition: transform 0.15s;
        }}
        .scan-btn:active {{ transform: scale(0.94); }}
        .scan-bar {{ width: 160px; height: 6px; background: #27272a; border-radius: 99px; margin-top: 16px; overflow: hidden; }}
        .scan-bar-fill {{ width: 0%; height: 100%; background: #f43f5e; transition: width 0.05s linear; }}

        /* Buttons & Options */
        .section-gap {{ display: flex; flex-direction: column; gap: 16px; }}
        .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 8px; }}
        .grid-1 {{ display: flex; flex-direction: column; gap: 8px; margin-top: 8px; }}
        .opt-btn {{
            background: #18181b; border: 1px solid #3f3f46; color: #f4f4f5;
            padding: 12px; border-radius: 12px; font-size: 13px;
            text-align: left; cursor: pointer; transition: all 0.2s;
            display: flex; justify-content: space-between; align-items: center;
        }}
        .opt-btn:hover {{ border-color: #f43f5e; }}
        .opt-selected {{ border-color: #fbbf24 !important; background: rgba(251, 191, 36, 0.15) !important; }}
        .quiz-selected {{ border-color: #f43f5e !important; background: rgba(244, 63, 94, 0.18) !important; }}

        .cta-btn {{
            width: 100%; padding: 15px; border: none; border-radius: 14px;
            font-size: 14px; font-weight: 800; cursor: pointer;
            background: linear-gradient(90deg, #f43f5e, #f59e0b);
            color: #ffffff; margin-top: 8px; transition: transform 0.15s;
        }}
        .cta-btn:active {{ transform: scale(0.97); }}
        .cta-white {{ background: #ffffff; color: #09090b; }}

        .no-btn {{
            background: #27272a; border: 1px solid #3f3f46; color: #a1a1aa;
            padding: 9px 18px; border-radius: 10px; font-size: 12px;
            cursor: pointer; margin-top: 10px; transition: transform 0.15s ease;
        }}

        /* Ticket */
        .ticket {{
            background: #09090b; border: 1px solid rgba(251, 191, 36, 0.55);
            border-radius: 16px; padding: 18px; margin-top: 14px;
        }}
        .ticket-row {{ margin-top: 12px; }}
        .ticket-label {{ font-size: 10px; color: #71717a; text-transform: uppercase; }}
        .ticket-val {{ font-size: 14px; font-weight: 700; margin-top: 2px; }}
        #confetti-canvas {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none; z-index: 50;
        }}
    </style>
</head>
<body>
    <canvas id="confetti-canvas"></canvas>

    <div class="container">
        <div class="progress-header mono">
            <span>FILE // {HER_NAME.upper()}</span>
            <span id="page-indicator">PAGE 01 / 04</span>
        </div>
        <div class="progress-track">
            <div id="progress-bar" class="progress-fill"></div>
        </div>

        <div class="card">
            <!-- PAGE 1 -->
            <section id="page-1" class="fade-in center">
                <span class="badge badge-rose mono">🔒 RESTRICTED ACCESS</span>
                <h1>Hey {HER_NAME}.</h1>
                <p class="sub">I, {YOUR_NAME}, built a classified file specifically for you. Verify your identity to unlock it.</p>

                <div class="scan-wrap">
                    <button id="scan-btn" type="button" class="scan-btn">
                        <span style="font-size: 34px; margin-bottom: 4px;">☝️</span>
                        <span id="scan-label" class="mono" style="font-size: 10px; font-weight: 700;">HOLD TO SCAN</span>
                    </button>
                    <div class="scan-bar"><div id="scan-fill" class="scan-bar-fill"></div></div>
                </div>

                <p id="scan-status" class="mono" style="font-size: 11px; color: #71717a;">Awaiting fingerprint verification...</p>
            </section>

            <!-- PAGE 2 -->
            <section id="page-2" class="hidden fade-in section-gap">
                <div>
                    <span class="mono" style="font-size: 11px; color: #fbbf24;">STEP 02 // COMPATIBILITY AUDIT</span>
                    <h2>Quick vibe check before we proceed.</h2>
                    <p class="sub">Be honest—the algorithm is judging.</p>
                </div>

                <div>
                    <p style="font-size: 13px; font-weight: 700;">1. What’s your ideal elite hangout?</p>
                    <div class="grid-2" id="q1-group">
                        <button type="button" onclick="selectQuiz('q1', this, 'Elite taste. Good food = good mood.')" class="opt-btn">🍜 Hidden food spot</button>
                        <button type="button" onclick="selectQuiz('q1', this, 'Main character energy. Respect.')" class="opt-btn">🌃 Night drive + music</button>
                        <button type="button" onclick="selectQuiz('q1', this, 'Cozy & undefeated combo.')" class="opt-btn">☕ Coffee & people-watch</button>
                        <button type="button" onclick="selectQuiz('q1', this, 'Competitive? Say less.')" class="opt-btn">🎳 Arcade / bowling</button>
                    </div>
                </div>

                <div>
                    <p style="font-size: 13px; font-weight: 700;">2. Who wins in Mario Kart / bowling?</p>
                    <div class="grid-2" id="q2-group">
                        <button type="button" onclick="selectQuiz('q2', this, 'Bold claim. We will test that theory.')" class="opt-btn">👑 Me, easily</button>
                        <button type="button" onclick="selectQuiz('q2', this, 'At least you are honest about it 😂')" class="opt-btn">😅 Probably {YOUR_NAME}</button>
                    </div>
                </div>

                <div id="quiz-feedback" class="mono center" style="min-height: 18px; font-size: 12px; color: #fda4af;"></div>

                <button type="button" onclick="goToPage(3)" class="cta-btn cta-white">Next: Customize Your Mission →</button>
            </section>

            <!-- PAGE 3 -->
            <section id="page-3" class="hidden fade-in section-gap">
                <div>
                    <span class="mono" style="font-size: 11px; color: #fbbf24;">STEP 03 // DESIGN THE PLAN</span>
                    <h2>Build your ideal hangout.</h2>
                    <p class="sub">Pick one from each section. {YOUR_NAME} handles the rest.</p>
                </div>

                <div>
                    <p class="mono" style="font-size: 11px; color: #a1a1aa;">THE VIBE</p>
                    <div class="grid-1" id="vibe-group">
                        <button type="button" onclick="selectPlan('vibe', this, 'Dinner & Late-Night Dessert 🍝🍨')" class="opt-btn opt-selected">🍝 Dinner & Late-Night Dessert</button>
                        <button type="button" onclick="selectPlan('vibe', this, 'Coffee Run & Sunset Walk ☕🌅')" class="opt-btn">☕ Coffee Run & Sunset Walk</button>
                        <button type="button" onclick="selectPlan('vibe', this, 'Drinks, Games & Trash Talk 🎳🏆')" class="opt-btn">🎳 Drinks, Games & Trash Talk</button>
                    </div>
                </div>

                <div>
                    <p class="mono" style="font-size: 11px; color: #a1a1aa;">THE WILDCARD RULE</p>
                    <div class="grid-2" id="rule-group">
                        <button type="button" onclick="selectPlan('rule', this, 'Phones on Do Not Disturb 📵')" class="opt-btn opt-selected">📵 Phones on DND</button>
                        <button type="button" onclick="selectPlan('rule', this, 'Winner picks dessert 🍦')" class="opt-btn">🍦 Winner picks dessert</button>
                    </div>
                </div>

                <button type="button" onclick="goToPage(4)" class="cta-btn">Lock In Choices & Reveal Finale ✨</button>
            </section>

            <!-- PAGE 4 -->
            <section id="page-4" class="hidden fade-in center">
                <div id="ask-view">
                    <span class="badge badge-amber mono">🎯 FINAL CLEARANCE GRANTED</span>
                    <h2>So {HER_NAME}... let’s make this official.</h2>
                    <p class="sub" style="margin: 12px 0 22px;">
                        You’re effortlessly cool,Probably fun to be around, and I’d love to take you out for an elite hangout or just an ice cream date. Are you in?
                    </p>

                    <button type="button" onclick="acceptDate()" class="cta-btn" style="font-size: 16px;">YES, I’M IN 🥂</button>
                    <div>
                        <button id="no-btn" type="button" onmouseover="dodgeNo()" onclick="dodgeNo()" class="no-btn">No thanks</button>
                    </div>
                </div>

                <div id="ticket-view" class="hidden fade-in">
                    <div style="font-size: 36px; margin-bottom: 6px;">🥂</div>
                    <h2>IT’S A DATE!</h2>
                    <p class="sub">Screenshot this pass and text it to {YOUR_NAME} to claim.</p>

                    <div class="ticket" style="text-align: left;">
                        <div style="display: flex; justify-content: space-between; font-size: 11px; border-bottom: 1px dashed #3f3f46; padding-bottom: 8px;" class="mono">
                            <span style="color: #fbbf24;">VIP DATE PASS // #001</span>
                            <span style="color: #4ade80;">CONFIRMED</span>
                        </div>
                        <div class="ticket-row">
                            <div class="ticket-label mono">GUESTS</div>
                            <div class="ticket-val">{HER_NAME} + {YOUR_NAME}</div>
                        </div>
                        <div class="ticket-row">
                            <div class="ticket-label mono">SELECTED VIBE</div>
                            <div id="ticket-vibe" class="ticket-val">Dinner & Late-Night Dessert 🍝🍨</div>
                        </div>
                        <div class="ticket-row">
                            <div class="ticket-label mono">WILDCARD RULE</div>
                            <div id="ticket-rule" class="ticket-val">Phones on Do Not Disturb 📵</div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </div>

    <script>
        let scanProgress = 0;
        let scanTimer = null;
        let selectedVibe = "Dinner & Late-Night Dessert 🍝🍨";
        let selectedRule = "Phones on Do Not Disturb 📵";
        let dodgeCount = 0;

        const scanBtn = document.getElementById("scan-btn");
        const scanFill = document.getElementById("scan-fill");
        const scanLabel = document.getElementById("scan-label");
        const scanStatus = document.getElementById("scan-status");

        function startScan(e) {{
            if (e) e.preventDefault();
            if (scanTimer) return;
            scanLabel.textContent = "SCANNING...";
            scanStatus.textContent = "Reading biometric signature...";
            scanStatus.style.color = "#fda4af";

            scanTimer = setInterval(() => {{
                scanProgress += 4;
                scanFill.style.width = scanProgress + "%";
                if (scanProgress >= 100) {{
                    clearInterval(scanTimer);
                    scanTimer = null;
                    scanLabel.textContent = "VERIFIED";
                    scanStatus.textContent = "Identity confirmed. Unlocking file...";
                    scanStatus.style.color = "#4ade80";
                    setTimeout(() => goToPage(2), 450);
                }}
            }}, 45);
        }}

        function cancelScan() {{
            if (scanProgress >= 100) return;
            clearInterval(scanTimer);
            scanTimer = null;
            scanProgress = 0;
            scanFill.style.width = "0%";
            scanLabel.textContent = "HOLD TO SCAN";
            scanStatus.textContent = "Scan interrupted. Hold down to verify...";
            scanStatus.style.color = "#71717a";
        }}

        scanBtn.addEventListener("mousedown", startScan);
        scanBtn.addEventListener("mouseup", cancelScan);
        scanBtn.addEventListener("mouseleave", cancelScan);
        scanBtn.addEventListener("touchstart", startScan, {{ passive: false }});
        scanBtn.addEventListener("touchend", cancelScan);
        scanBtn.addEventListener("touchcancel", cancelScan);

        function goToPage(pageNum) {{
            for (let i = 1; i <= 4; i++) {{
                document.getElementById("page-" + i).classList.add("hidden");
            }}
            document.getElementById("page-" + pageNum).classList.remove("hidden");
            document.getElementById("page-indicator").textContent = "PAGE 0" + pageNum + " / 04";
            document.getElementById("progress-bar").style.width = (pageNum * 25) + "%";
        }}

        function selectQuiz(group, btn, feedback) {{
            const buttons = document.querySelectorAll("#" + group + "-group .opt-btn");
            buttons.forEach(b => b.classList.remove("quiz-selected"));
            btn.classList.add("quiz-selected");
            document.getElementById("quiz-feedback").textContent = feedback;
        }}

        function selectPlan(type, btn, value) {{
            const groupId = type === "vibe" ? "vibe-group" : "rule-group";
            const buttons = document.querySelectorAll("#" + groupId + " .opt-btn");
            buttons.forEach(b => b.classList.remove("opt-selected"));
            btn.classList.add("opt-selected");

            if (type === "vibe") {{
                selectedVibe = value;
                document.getElementById("ticket-vibe").textContent = value;
            }} else {{
                selectedRule = value;
                document.getElementById("ticket-rule").textContent = value;
            }}
        }}

        function dodgeNo() {{
            dodgeCount++;
            const noBtn = document.getElementById("no-btn");
            const x = Math.floor(Math.random() * 140) - 70;
            const y = Math.floor(Math.random() * 90) - 45;
            noBtn.style.transform = `translate(${{x}}px, ${{y}}px)`;
            if (dodgeCount >= 3) {{
                noBtn.textContent = "Nice try 😂";
            }}
        }}

        function acceptDate() {{
            document.getElementById("ask-view").classList.add("hidden");
            document.getElementById("ticket-view").classList.remove("hidden");
            launchConfetti();
        }}

        function launchConfetti() {{
            const canvas = document.getElementById("confetti-canvas");
            const ctx = canvas.getContext("2d");
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            const pieces = Array.from({{ length: 80 }}, () => ({{
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height - canvas.height,
                r: Math.random() * 6 + 4,
                c: ["#f43f5e", "#fbbf24", "#4ade80", "#38bdf8"][Math.floor(Math.random() * 4)],
                v: Math.random() * 3 + 2
            }}));
            function draw() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                pieces.forEach(p => {{
                    ctx.fillStyle = p.c;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                    ctx.fill();
                    p.y += p.v;
                    if (p.y > canvas.height) p.y = -10;
                }});
                requestAnimationFrame(draw);
            }}
            draw();
        }}
    </script>
</body>
</html>"""
    return HTMLResponse(content=html)
