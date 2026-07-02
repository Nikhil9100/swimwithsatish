import sys

HTML_CONTENT = """
  <!-- ═══════════════════════════════════════════════════ BENEFITS OF SWIMMING -->
  <section id="benefits" style="position: relative; padding: 120px 5vw; background: linear-gradient(to bottom, #02040a, #060d1f);">
    <!-- Decorative background elements -->
    <div style="position: absolute; top: -150px; right: -150px; width: 600px; height: 600px; border-radius: 50%; background: radial-gradient(circle, rgba(14,165,233,0.04) 0%, transparent 70%); pointer-events: none;"></div>
    
    <div class="benefits-header" style="text-align: center; margin-bottom: 4rem; position: relative; z-index: 2;">
      <div class="section-label reveal">Why Swim?</div>
      <h2 class="section-title reveal reveal-delay-1">The Ultimate <em>Superpower</em></h2>
      <div class="divider reveal reveal-delay-2" style="margin: 1.5rem auto 2rem; background: linear-gradient(135deg, #0ea5e9 0%, #38bdf8 100%); width: 80px; height: 4px;"></div>
      <p class="section-sub reveal reveal-delay-3" style="max-width: 700px; margin: 0 auto; color: #94a3b8; font-size: 1.15rem; line-height: 1.6;">Swimming isn't just a sport; it's a life-saving skill and one of the most effective ways to transform your physical and mental health.</p>
    </div>

    <style>
      .benefits-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
      }
      .benefit-card {
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 1.5rem;
        padding: 2.5rem 2rem;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-align: left;
        position: relative;
        overflow: hidden;
      }
      .benefit-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(135deg, rgba(14,165,233,0.1), transparent);
        opacity: 0;
        transition: opacity 0.4s ease;
      }
      .benefit-card:hover {
        transform: translateY(-10px);
        border-color: rgba(14, 165, 233, 0.3);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 20px rgba(14,165,233,0.1);
      }
      .benefit-card:hover::before {
        opacity: 1;
      }
      .benefit-icon-wrapper {
        width: 64px;
        height: 64px;
        border-radius: 1rem;
        background: rgba(14, 165, 233, 0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1.5rem;
        color: #0ea5e9;
        transition: all 0.3s ease;
      }
      .benefit-card:hover .benefit-icon-wrapper {
        background: #0ea5e9;
        color: #fff;
        transform: scale(1.1) rotate(5deg);
      }
      .benefit-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 1rem;
        font-family: 'Outfit', sans-serif;
      }
      .benefit-desc {
        color: #94a3b8;
        font-size: 1rem;
        line-height: 1.6;
      }
    </style>

    <div class="benefits-grid">
      <!-- Card 1 -->
      <div class="benefit-card reveal">
        <div class="benefit-icon-wrapper">
          <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
        </div>
        <h3 class="benefit-title">Full-Body Workout</h3>
        <p class="benefit-desc">Engages almost every major muscle group in your body. It tones muscles, builds strength, and improves overall endurance simultaneously.</p>
      </div>

      <!-- Card 2 -->
      <div class="benefit-card reveal reveal-delay-1">
        <div class="benefit-icon-wrapper">
          <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
        </div>
        <h3 class="benefit-title">Cardio & Heart Health</h3>
        <p class="benefit-desc">Makes your heart and lungs incredibly strong. Regular swimming lowers blood pressure and significantly reduces the risk of heart disease.</p>
      </div>

      <!-- Card 3 -->
      <div class="benefit-card reveal reveal-delay-2">
        <div class="benefit-icon-wrapper">
          <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
        </div>
        <h3 class="benefit-title">Zero Impact & Safe</h3>
        <p class="benefit-desc">Water provides buoyancy, eliminating stress on your joints and bones. It's the perfect sport for injury recovery, arthritis, and all ages.</p>
      </div>

      <!-- Card 4 -->
      <div class="benefit-card reveal">
        <div class="benefit-icon-wrapper">
          <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        </div>
        <h3 class="benefit-title">Stress Relief</h3>
        <p class="benefit-desc">The rhythmic nature of swimming and the soothing feel of water triggers endorphins, drastically reducing stress, anxiety, and depression.</p>
      </div>

      <!-- Card 5 -->
      <div class="benefit-card reveal reveal-delay-1">
        <div class="benefit-icon-wrapper">
          <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
        </div>
        <h3 class="benefit-title">Better Sleep Quality</h3>
        <p class="benefit-desc">Struggling with insomnia? The energy exertion and full-body relaxation involved in swimming have been proven to promote deeper, better sleep.</p>
      </div>

      <!-- Card 6 -->
      <div class="benefit-card reveal reveal-delay-2">
        <div class="benefit-icon-wrapper">
          <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
        </div>
        <h3 class="benefit-title">Lifesaving Skill</h3>
        <p class="benefit-desc">Beyond fitness, swimming equips you with crucial survival skills. It builds immense confidence in and around water environments.</p>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ COURSES -->
"""

with open('/home/nikhil/swimwithsatish/index.html', 'r') as f:
    content = f.read()

target = '<!-- ═══════════════════════════════════════════════════ COURSES -->'
if target in content:
    new_content = content.replace(target, HTML_CONTENT)
    with open('/home/nikhil/swimwithsatish/index.html', 'w') as f:
        f.write(new_content)
    print("Success")
else:
    print("Target not found")
