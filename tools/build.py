#!/usr/bin/env python3
"""Generates the static pages. Content is verbatim from priscillagrijalva.com."""
import json, html, os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L=json.load(open(os.path.join(R,'tools/lists.json')))
I='assets/img/'
e=html.escape
NAV=[('Bio','bio.html'),('Book','book.html'),('Keynotes','speaking-1.html'),('Thought Leadership','media.html'),('Presentations','presentations-and-workshops.html'),('Media','media-1.html'),('Testimonials','reviews-and-testimonies.html'),('Gallery','gallery.html'),('Contact','contact.html')]
def page(fn,title,body):
    nav=''.join(f'<a href="{h}"{" class=nav-cta" if h=="contact.html" else ""}{" aria-current=page" if h==fn else ""}>{t}</a>' for t,h in NAV)
    out=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css"></head><body>
<a class="skip" href="#page">Skip to Content</a>
<header class="site-header"><div class="wrap hbar"><a class="brand" href="index.html">Priscilla A. Grijalva</a>
<button class="menu-btn" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
<nav class="nav">{nav}</nav></div></header>
<main id="page">{body}</main>
<footer class="site-footer"><div class="wrap fgrid"><div><a class="brand light" href="index.html">Priscilla A. Grijalva</a><p class="fine">Grijalva Education Consulting LLC ™</p></div>
<nav class="fnav">{nav}</nav></div></footer>
<script src="assets/js/main.js"></script></body></html>'''
    open(os.path.join(R,fn),'w').write(out)
def hero(kicker,title,sub=''):
    return f'<section class="phero"><div class="wrap"><p class="kicker">{kicker}</p><h1>{title}</h1>{f"<p class=lede>{sub}</p>" if sub else ""}</div></section>'
EXT='target="_blank" rel="noopener"'
VIDS='<div class="videos">  <figure><div class="vid"><iframe src="https://www.youtube.com/embed/ZvJB_HISdPU" title="NACAC 2022" allowfullscreen loading="lazy"></iframe></div>   <figcaption><a href="https://youtu.be/ZvJB_HISdPU?si=wdtx_RJXNUgXuaqW" '+EXT+'>Speaking on the Main Stage at the 2022 NACAC conference</a></figcaption></figure>  <figure><div class="vid"><iframe src="https://www.youtube.com/embed/kmcKiD-HYjA" title="Former students on stage with Former First Lady, Michelle Obama" allowfullscreen loading="lazy"></iframe></div>   <figcaption><a href="https://youtube.com/shorts/kmcKiD-HYjA?si=c-FeRawxIiKSSMP9" '+EXT+'>Former students on stage with Former First Lady, Michelle Obama</a></figcaption></figure> </div>'

# HOME
page('index.html','Priscilla A. Grijalva',f'''
<section class="hero"><div class="wrap hero-grid">
 <div class="hero-text"><p class="kicker">Priscilla A. Grijalva</p><h1>Building Systems of Hope.</h1>
 <p class="tagline">Keynote Speaker | International and National Award Winning School Counselor | Author | Presenter</p>
 <div class="btns"><a class="btn" href="contact.html">Contact</a><a class="btn ghost" href="speaking-1.html">Keynotes &amp; Speeches</a></div></div>
 <div class="hero-img"><img src="{I}c5d86e70-updated.png" alt="Priscilla A. Grijalva"></div>
</div></section>
<section class="band blush"><div class="wrap split">
 <div class="split-img"><img src="{I}d09942e5-8feb2afe-dec7-43ca-8141-76abfdc5369c.png" alt=""></div>
 <div><p class="big">As a first-generation college student and Latina school counselor, my purpose is to advance equity, inclusion, and social justice in education. I partner with schools, school counselors, educators, and organizations to expand access to postsecondary opportunities, strengthen equitable practices, and create systems that support student success. Through consulting, professional learning, and advocacy, I work to amplify the voices of historically underrepresented and underserved students and help ensure that each and every student has access to the opportunities, resources, and support they need to be successful.</p></div>
</div></section>
<section class="band watch"><div class="wrap feature-vid">
 <div class="fv-text"><h2 class="sec">Watch</h2><p>Speaking on the Main Stage at the 2022 NACAC conference.</p><a class="btn" href="https://youtu.be/ZvJB_HISdPU?t=74" target="_blank" rel="noopener">Watch on YouTube</a></div>
 <div class="vid"><button class="vid-cover" aria-label="Play NACAC 2022 Main Stage" onclick="this.outerHTML='<iframe src=&quot;https://www.youtube.com/embed/ZvJB_HISdPU?start=74&amp;autoplay=1&quot; title=&quot;NACAC 2022 Main Stage&quot; allow=&quot;autoplay; fullscreen&quot; allowfullscreen></iframe>'"><img src="assets/img/nacac-cover.png" alt="Priscilla speaking on the NACAC 2022 main stage"><span class="play"></span></button></div>
</div></section>
<section class="band dark"><div class="wrap cta"><h2>Let’s Build Systems of Hope Together!</h2>
<p>Whether you are planning a conference, exploring professional learning opportunities, or looking for ways to strengthen student support systems, I’d welcome the opportunity to connect and collaborate!</p>
<a class="btn light" href="contact.html">Contact</a></div></section>''')

# BIO
def ul(items): return '<ul class="clean">'+''.join(f'<li>{x}</li>' for x in items)+'</ul>'
rec=["2026 — American Counseling Association Counselors for Social Justice Ohana Award Recipient","2025 — American School Counselor Association Distinguished Professional Award","2025 — Bezos Scholar Educator","2025, 2023, 2021, 2020, 2015 – Five-Time California School Counselor of the Year Nominee (2015 Finalist)","2023 — California Woman of the Year","2023 — Award of Excellence, Professional School Counselors of Color","2022 — National Life Changer of the Year","2021 — When We All Vote Hispanic Heritage Month Recognition","2020 — Reach Higher Latinx Heritage Month Recognition","2020 — National College Board Counselor Award","2018 — U.S. Air Force Distinguished Educator","2015 — University of California Early Academic Outreach Program Counselor of the Year","2011 — U.S. Navy Educator Award"]
def recli(x):
    y,_,t=x.partition(' — ') if ' — ' in x else x.partition(' – ')
    return f'<li><span class="yr">{y}</span><span>{t}</span></li>'
edu=["Administrative Services Credential, University of Redlands","Pupil Personnel Services Credential, University of Redlands","M.S., Counseling Psychology, California Baptist University","B.A., Political Science, California Baptist University"]
cert=["American School Counselor Association (ASCA) Certified School Counselor","Pennsylvania Education Specialist I","ASCA Diversity, Equity, and Inclusion Specialist","ASCA School Counseling Association Leadership Specialist"]
team=["Recognized ASCA Model Program (RAMP) 2X recipient, 2023 &amp; 2025","National Postsecondary Strategy Institute Reach Higher Power of Hope Award, 2021","When We All Vote, MTV Champion, 2020"]
page('bio.html','Bio — Priscilla A. Grijalva',hero('Bio','About Priscilla A. Grijalva')+f'''
<section class="band"><div class="wrap bio">
<aside class="bio-side"><img class="portrait" src="{I}bb8c48f5-293766368_10158690024188457_73129225213965542_n.jpg" alt="Priscilla A. Grijalva">
<a class="li-link" href="https://www.linkedin.com/in/priscilla-grijalva-0228591a4/" {EXT}><img src="{I}5e16b6bf-download.png" alt="LinkedIn"></a></aside>
<div class="prose">
<p><strong>Priscilla A. Grijalva</strong> is a high school counselor, educational leader, author, and advocate with more than 20 years of experience supporting students at the middle and high school levels. Her work is grounded in a deep commitment to equity, access, belonging, and expanding postsecondary opportunities for each and every student. She believes that when young people are seen, supported, and provided with clear pathways to success, their lives and the communities around them can be transformed.</p>
<p>Throughout her career, Priscilla has designed and led comprehensive, data-driven school counseling programs that elevate student voice, strengthen school communities, and create lasting systemic change. She has guided two schools to earn their first-ever Recognized ASCA Model Program (RAMP) designation, including one that became the first school in its district to receive the recognition. She has also helped lead districtwide initiatives focused on college and career access, equity, civic engagement, student leadership, and inclusive school culture.</p>
<p>Priscilla’s leadership extends beyond her school community. She has served on the American School Counselor Association Board of Directors and as a university adjunct instructor, University of California application reader, TN Achieves mentor, high school basketball coach, and host of the educational podcast <em>Reach Higher Riverside</em>. She has also contributed to equity-focused leadership teams and initiatives designed to strengthen belonging and educational opportunity for students.</p>
<p>A sought-after speaker and presenter, Priscilla has shared her work at state and national conferences, including as a main-stage speaker at the National Association for College Admission Counseling (NACAC) Conference. She has also delivered the keynote address at the University of Redlands Students of Color Commencement Ceremony. Her student-centered leadership and advocacy have been recognized at the state, national, and international levels.</p>
<p>Above all, Priscilla is passionate about helping each and every student recognize their potential, embrace their identities, and pursue futures they may not have imagined for themselves. Through counseling, leadership, advocacy, and education, she continues to champion systems that open doors, expand opportunity, inspire possibility, and empower young people to shape their own futures.</p>
</div></div></section>
<section class="band blush"><div class="wrap"><h2 class="sec">STATE, NATIONAL &amp; INTERNATIONAL RECOGNITIONS</h2><ul class="awards">{''.join(recli(x) for x in rec)}</ul></div></section>
<section class="band"><div class="wrap cols3">
<div class="card"><h3 class="ih"><svg class="ico" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#9c4a2f" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/><path d="M22 9v5"/></svg><span>EDUCATION</span></h3>{ul(edu)}</div><div class="card"><h3 class="ih"><svg class="ico" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#9c4a2f" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M7 8h10M7 11h6"/><circle cx="16" cy="17" r="2.5"/><path d="M14.8 19l-.8 3 2-1 2 1-.8-3"/></svg><span>CERTIFICATIONS</span></h3>{ul(cert)}</div><div class="card"><h3 class="ih"><svg class="ico" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#9c4a2f" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="15" r="5"/><path d="M8.5 11.5L6 3h4l2 5 2-5h4l-2.5 8.5"/><path d="M12 13l.8 1.6 1.7.2-1.2 1.2.3 1.7-1.6-.8-1.6.8.3-1.7-1.2-1.2 1.7-.2z"/></svg><span>NATIONAL TEAM RECOGNITIONS</span></h3>{ul(team)}</div>
</div></section>''')

# SPEAKING
sp=L['speak'][1:]
page('speaking-1.html','Keynotes &amp; Speeches — Priscilla A. Grijalva',hero('Speaking','Keynotes &amp; Speeches')+f'''
<section class="band"><div class="wrap split top"><div class="split-img"><img src="{I}c4585497-pix3.jpg" alt=""></div>
<ol class="timeline">{''.join(f"<li>{e(x)}</li>" for x in sp)}</ol></div></section>''')

# BOOK
bl=["Build schoolwide systems that expand postsecondary opportunities","Use data to identify and close equity gaps","Demystify financial aid and scholarship pathways","Implement MTSS frameworks to support college and career readiness","Create partnerships with colleges, military recruiters, and community organizations","Celebrate student success in ways that foster belonging and hope"]
page('book.html','Book — Priscilla A. Grijalva',hero('Book','#1 New Release Best Seller on Amazon for College Counseling, Financial Aid, and Career Development Counseling!')+f'''
<section class="band"><div class="wrap book">
<div class="cover"><img src="{I}5e20eb6d-10-lessons-ebook-2.jpg" alt="10 Lessons for Postsecondary Access"></div>
<div class="prose"><p class="big">This practical guide provides both inspiration and actionable strategies for educators committed to equity and student success.</p>
<p><strong>Inside this book, you will learn how to:</strong></p><ul class="checks">{''.join(f"<li>{x}</li>" for x in bl)}</ul>
<p>Through real-world stories, replicable strategies, and leadership insights, this book offers a clear roadmap for school counselors, counselor educators, and graduate students who are committed to ensuring every student—especially those historically underserved—has access to meaningful postsecondary pathways.</p>
<h3>A Message of Hope</h3>
<p>At its core, <em>10 Lessons for Postsecondary Access</em> reminds educators that when hope is paired with intentional systems, students thrive—and entire communities can change.</p>
<div class="btns"><a class="btn" href="https://a.co/d/09HybLFw" {EXT}>Amazon</a><a class="btn ghost" href="https://www.barnesandnoble.com/w/10-lessons-for-postsecondary-access-priscilla-grijalva/1150237071?ean=9798234047403" {EXT}>Barnes and Noble</a></div>
</div></div></section>''')

# THOUGHT LEADERSHIP (caption/image pairing follows the original's visual layout)
art=[("NACAC Journal: Co-authored article. Pages 16-18","https://online.flippingbook.com/view/177945395","4418dabd-screenshot-2026-07-20-134434.png"),
("Forbes BrandVoice Article","https://www.forbes.com/sites/civicnation/2018/03/02/norte-vista-high-school-reaches-higher/#11593632125b","203cece9-link.2.png"),
("Link for Counselors Article","https://www.linkforcounselors.com/beyond-the-court-how-title-ix-changed-my-life/","a7522a0b-link.2.png"),
("Link for Counselors Magazine: Co-Authored article. Pages 34-37","https://bt.e-ditionsbyfry.com/publication/?i=860424&amp;p=1&amp;pp=1&amp;view=issueViewer","7448e021-link.png"),
("","https://ccnow.sdsu.edu/reach-higher-stories-from-riverside-ca/","da83e306-screenshot-2026-07-20-134434.png"),
("University of California Article","https://mailchi.mp/ucop/hsa-bulletin-jan-2020?e=ea9bc02d24","af9d8b6b-link.2.png"),
("Link for Counselors Magazine: pages 10-11","https://bt.e-ditionsbyfry.com/publication/?i=804597&amp;p=1&amp;view=issueViewer&amp;pp=1","1d06e165-link.png"),
("Link for Counselors Magazine Co-Authored article. Pages 18-21","https://bt.e-ditionsbyfry.com/publication/?i=839845&amp;p=1&amp;pp=1&amp;view=issueViewer","e9ef97a7-link.png"),
("Contributor for the Washington Post","https://www.washingtonpost.com/education/2024/03/18/sat-test-policies-confuse-students/","20470e74-images.jpg"),
("Bezos Scholars Program (last article)","https://www.bezosscholars.org/story/abundance-in-aspen","939167f4-images.jpg"),
("Article featured across all state school counselor association newsletters)","https://www.schoolcounselor.org/Newsletters/November-2023/noCreating-a-Culture-of-Successful-Postsecondary-T?st=TX&amp;_zs=FT5Hl1&amp;_zl=l4EI9","4cd8cf58-screenshot-2026-07-20-134834.png"),
("","https://www.higheredjobs.com/Articles/articleDisplay.cfm?ID=4781&amp;Title=Beyond%20Recruitment%3A%205%20Ways%20Colleges%20Can%20Become%20True%20Partners%20with%20High%20School%20Counselors","e370041f-img_6173.jpg"),
("Link for Counselors Magazine: pages 44-45","https://bt.e-ditionsbyfry.com/publication/?i=870794&amp;p=1&amp;view=issueViewer&amp;fbclid=IwY2xjawVCgvFleHRuA2FlbQIxMABwZG9mBWJyaWQRMXJDNnlKcHp6UFZaYU1XbFZzcnRjBmFwcF9pZBAyMjIwMzkxNzg4MjAwODkyAAEe0dGku98OF5OUKr6vDad6ZBEratOB69WGzOHsfm5c23GaNc2TPM3vMXDGJXE_aem_qlfTT4ZmqP0IaJwsedEoyQ","29b4c90c-img_7290.jpg")]
def card(c,u,i): return f'<a class="tile" href="{u}" {EXT}><div class="thumb"><img src="{I}{i}" alt="{c}" loading="lazy"></div>{f"<p>{c}</p>" if c else ""}</a>'
page('media.html','Thought Leadership — Priscilla A. Grijalva',hero('Thought Leadership','Thought Leadership','<a href="media.html">Priscilla often contributes to magazines and mainstream media.  Here are examples of articles!</a>')+
 f'<section class="band"><div class="wrap tiles">{"".join(card(*a) for a in art)}</div></section>')

# MEDIA

pods=[("https://podcasts.apple.com/us/podcast/the-power-of-advocacy-how-school-counselors-can/id1469569875?i=1000674738785","f157742d-link.png"),
("https://open.spotify.com/episode/4JBIDLI5fITdqcafxhYqa5","a64336b6-link.png"),
("https://open.spotify.com/episode/5rY4nm45RQLTS29dREBbnM?si=qRFmenSPS6KjdQDhwAocFg","354bcda5-kheaa.png"),
("https://podcasts.apple.com/us/podcast/priscilla-grijalva/id1474469699?i=1000766277200","7bc4055c-link.png"),
("https://youtu.be/JAcy9Qyqi5Q?si=uwZlchRx1Bs_K9U_","6380a8c2-link.png"),
("https://podcasts.apple.com/us/podcast/school-counselor-advocacy-and-empowering-students-for/id1596980312?i=1000629047426","0c438137-link.png"),
("https://podcasts.apple.com/us/podcast/beyond-guidance-reaching-beyond-to-support-school-counselors/id1649121266?i=1000605077996","6f601e97-link.png"),
("https://podcasts.apple.com/us/podcast/priscilla-grijalva-on-helping-kids-with-lifes-journey/id1512600888?i=1000553884108","d1a51723-link.png")]
page('media-1.html','Media — Priscilla A. Grijalva',hero('Podcasts &amp; Interviews','Media','Priscilla often lends a voice to the media to address issues and advocate for school counseling, financial aid, and college access. Watch these videos and listen to these podcasts to learn more.')+
 f'<section class="band"><div class="wrap"><h2 class="sec">Listen</h2><div class="tiles">{"".join(card("",u,i) for u,i in pods)}</div></div></section><section class="band watch follow"><div class="wrap"><h2 class="sec">Watch</h2>{VIDS}</div></section>')

# PRESENTATIONS
pr=L['pres'][1:]
page('presentations-and-workshops.html','Presentations — Priscilla A. Grijalva',hero('Presentations','Local, State, and National Presentations')+
 f'<section class="band"><div class="wrap"><ol class="timeline two">{"".join(f"<li>{e(x)}</li>" for x in pr)}</ol></div></section>')

# TESTIMONIES
q=lambda t,w: f'<figure class="quote"><blockquote>{t}</blockquote><figcaption>{w}</figcaption></figure>'
page('reviews-and-testimonies.html','Testimonies — Priscilla A. Grijalva',hero('Testimonies','What Attendees Are Saying')+f'''
<section class="band"><div class="wrap quotes">
{q("“The presenter was awesome!”","-California Association of School Counselors Conference Attendee-")}
{q("“One of the best presenters at ASCA!”","-American School Counselor Association Conference Attendee")}
{q("“I had been struggling for months as a College Advisor while doing the work of three counselors. Priscilla’s words reminded me that the sacrifice is 100% worth it. Her NACAC presentations were inspiring and left me with new ideas and an even stronger determination to do what I know I need to do. Her words truly made a difference.”","-College Advisor, National Association for College Admission Counseling Conference Attendee")}
{q("“Engaging Main Stage Speaker.”","- National Association for College Admission Counseling Conference Attendee")}
{q("“Great content, practical ideas, and meaningful strategies for helping every student feel seen, heard, and celebrated.”","-Nebraska EducationQuest Keynote Attendee")}
</div></section>
<section class="band dark"><div class="wrap stats">
<div><h2>100% Session Satisfaction</h2><p>Attendees described Priscilla’s session as practical, innovative, and immediately applicable, highlighting strategies that could be implemented in both small rural and large urban schools.</p><p>They especially valued learning not only what to implement, but the why, strategy, implementation, and data behind the programming. -Nebraska EducationQuest Keynote Attendee Feedback</p></div>
<div><h2>100% Positive Evaluation Responses</h2><p>100% of evaluation respondents rated the session positively across every measure, including relevance, inclusivity, opportunities for collaboration, and preparedness to apply what they learned.</p></div>
<div><h2>Engaging. Authentic. Full of Energy.</h2><p>Attendee feedback highlighted Priscilla’s storytelling, personal connection, clear delivery, intentional flow, and contagious enthusiasm—creating a presentation experience that was both engaging and memorable. -Bezos Scholars Program HERO MD Virtual Attendee Feedback</p></div>
</div></section>
<section class="band"><div class="wrap quotes">
{q("“This was an amazing presentation. It uplifted Latino educators who are facing many barriers when it comes to education and SEL implementation.”","-National School Counseling Leadership Conference Attendee")}
{q("“As a recruiter for the Army, I’ve seen many counselors, but Priscilla stands out for her commitment to putting students first.”","-U.S. Army Recruiter Book Reviewer")}
</div></section>''')

# GALLERY
g=["ca0e7dd0-pix4.jpg","c5e8f2fc-img_5782.jpg","97204fdf-img_5782.jpg","41f562c3-pix2.jpeg","8f3758b1-pix6.jpg","c6f94181-img_5782.jpg","09f8af7f-img_5782.jpg","f3e925f0-pix1.jpeg","7c3a277a-pix3.jpg","a071bafe-img_5782.jpg","1e1bff1e-img_5782.jpg"]
page('gallery.html','Gallery — Priscilla A. Grijalva',hero('Gallery','Gallery')+
 f'<section class="band"><div class="wrap masonry">{"".join(f"<a href={I}{x} class=gimg><img src={I}{x} alt=\"\" loading=lazy></a>" for x in g)}</div></section>')

# CONTACT
page('contact.html','Contact — Priscilla A. Grijalva',f'''
<section class="band contact"><div class="wrap split">
<div><p class="kicker">Contact</p><h1 class="display">Let’s connect! Contact Priscilla for keynote speaking engagements and presentations.</h1>
<form class="form" onsubmit="event.preventDefault();this.querySelector('.note').hidden=false">
<div class="row"><label>First Name<input name="fname" required></label><label>Last Name<input name="lname" required></label></div>
<label>Email<input type="email" name="email" required></label>
<label>Message<textarea name="message" rows="5" required></textarea></label>
<button class="btn" type="submit">Submit</button><p class="note fine" hidden>Preview only: this form is not connected yet.</p></form></div>
<div class="split-img"><img src="{I}86969c76-pix2.jpg" alt=""></div></div></section>''')
print('built')
