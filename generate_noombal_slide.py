import json

# Data for Noombal Location Pin (13°03'33.6"N 80°08'00.0"E)
noombal_data = [
    {
        "id": "it",
        "name": "IT Parks & Business Hubs",
        "count": 7,
        "color": "#2563EB",
        "sub": "Dual-corridor employment access to Porur tech spine and Ambattur industrial/IT zone",
        "items": [
            {
                "name": "Commerzone Porur",
                "distance": "6.9km",
                "time": "18 mins",
                "image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1000&q=80",
                "importance": "Grade-A IT park campus hosting multinational software & BPO giants. Direct arterial connection via Chennai Bypass drives immediate rental demand for residential units.",
                "demographic": "IT Consultants, Tech Leads & Software Engineers",
                "catalyst": "High-Density White-Collar Rental Tenant Inflow"
            },
            {
                "name": "RMZ One Paramount (Porur)",
                "distance": "6.8km",
                "time": "18 mins",
                "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1000&q=80",
                "importance": "2.4M sq.ft. LEED Platinum campus hosting Amazon, Caterpillar & Hitachi. Anchors executive and managerial tenant demand within an 18-minute drive.",
                "demographic": "Global MNC Executives & Corporate Managers",
                "catalyst": "Premium Rental Yields & High Tenancy Stability"
            },
            {
                "name": "L&T Infotech / SEZ Campus",
                "distance": "8.5km",
                "time": "22 mins",
                "image": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&w=1000&q=80",
                "importance": "Over 30,000 corporate engineering professionals seeking tranquil family housing outside congested city zones, ensuring zero vacancy risk.",
                "demographic": "Engineering Leads & Enterprise Developers",
                "catalyst": "Long-term Corporate Lease Renewals"
            },
            {
                "name": "D.L.F Cyber City (DLF IT Park)",
                "distance": "9.0km",
                "time": "24 mins",
                "image": "https://images.unsplash.com/photo-1554469384-e58fac16e23a?auto=format&fit=crop&w=1000&q=80",
                "importance": "Chennai's benchmark IT destination with 70,000+ employees; the primary engine of high rental yields (4.5%–5.2%) in the greater southwest corridor.",
                "demographic": "Massive Corporate IT Workforce with High Spending Power",
                "catalyst": "Benchmark Real Estate Rental Engine"
            },
            {
                "name": "Kosmo One IT Park - Ambattur",
                "distance": "9.7km",
                "time": "22 mins",
                "image": "https://images.unsplash.com/photo-1577495508048-b635879837f1?auto=format&fit=crop&w=1000&q=80",
                "importance": "North-West Chennai's premier 10-acre Grade-A IT park housing global financial services, healthcare tech, and IT operations.",
                "demographic": "Fintech, Back-Office Leadership & IT Architects",
                "catalyst": "Unlocks Ambattur IT Corridor Rental Catchment"
            },
            {
                "name": "Ambit IT Park (Ambattur Industrial Estate)",
                "distance": "9.9km",
                "time": "23 mins",
                "image": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1000&q=80",
                "importance": "Key modern tech park within the Ambattur Industrial corridor, easily accessible via Chennai Bypass avoiding inner-city traffic bottlenecks.",
                "demographic": "Industrial Tech Executives & Operations Managers",
                "catalyst": "Seamless Bypass Access to Ambattur Industrial Corridor"
            },
            {
                "name": "Olympia Technology Park (Guindy)",
                "distance": "12.3km",
                "time": "30 mins",
                "image": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1000&q=80",
                "importance": "Flagship CBD-periphery tech hub connected directly via arterial roads, bridging central city corporate hubs to the western suburbs.",
                "demographic": "Senior Corporate Management & CXO Leadership",
                "catalyst": "Direct Arterial Link to Established City Center"
            }
        ]
    },
    {
        "id": "schools",
        "name": "Schools & Colleges",
        "count": 8,
        "color": "#D97706",
        "sub": "Cluster of premier medical colleges, deemed universities, and international schools",
        "items": [
            {
                "name": "ACS Medical College & Hospital",
                "distance": "1.7km",
                "time": "3 mins",
                "image": "https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&w=1000&q=80",
                "importance": "Prominent medical college and teaching hospital campus situated right along Poonamallee High Road, generating continuous faculty and student rental demand.",
                "demographic": "Medical Professors, Lecturers & Resident Students",
                "catalyst": "Steady Year-round Institutional Rental Demand"
            },
            {
                "name": "Sindhi College (Thiruverkadu)",
                "distance": "2.0km",
                "time": "3 mins",
                "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1000&q=80",
                "importance": "Established arts, science, and management college in Thiruverkadu anchoring the youth academic demographic in the immediate vicinity.",
                "demographic": "College Staff, Faculty & Students",
                "catalyst": "Localized Educational Anchor for Suburban Catchment"
            },
            {
                "name": "The Pupil Saveetha Eco School",
                "distance": "3.8km",
                "time": "8 mins",
                "image": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=1000&q=80",
                "importance": "Prestigious eco-friendly CBSE school with world-class sprawling campus and sports infrastructure, serving as a decisive magnet for young families.",
                "demographic": "Young Nuclear Families & Progressive Parents",
                "catalyst": "High-Value School Proximity Driving Home Conversions"
            },
            {
                "name": "Sri Ramachandra Institute of Higher Education (SRMC)",
                "distance": "3.8km",
                "time": "12 mins",
                "image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1000&q=80",
                "importance": "Nationally ranked Deemed Medical University with thousands of postgraduate resident doctors, researchers, and faculty ensuring zero rental vacancy.",
                "demographic": "Resident Doctors, Healthcare Researchers & Professors",
                "catalyst": "Perpetual, High-Yield Healthcare Rental Market"
            },
            {
                "name": "Saveetha Dental College & Hospitals",
                "distance": "4.3km",
                "time": "9 mins",
                "image": "https://images.unsplash.com/photo-1577896851231-70ef18881754?auto=format&fit=crop&w=1000&q=80",
                "importance": "Global top-ranked dental education institution generating steady demand for premium apartments from international and domestic postgraduates.",
                "demographic": "Dental Scholars, Clinicians & Academic Staff",
                "catalyst": "International & Domestic Student Housing Demand"
            },
            {
                "name": "The Schram Academy (Maduravoyal)",
                "distance": "6.0km",
                "time": "17 mins",
                "image": "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=1000&q=80",
                "importance": "Leading international CBSE/Cambridge day school with excellent academic track record, popular with upwardly mobile corporate parents.",
                "demographic": "Mid-to-Senior Level Corporate Professionals",
                "catalyst": "Expands Premium Schooling Options within Reach"
            },
            {
                "name": "Velammal Vidyalaya (Ayanambakkam / Vanagaram)",
                "distance": "6.7km",
                "time": "18 mins",
                "image": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=1000&q=80",
                "importance": "Highly sought-after academic institution known for competitive exam preparation and academic rigour; commands high residential loyalty.",
                "demographic": "Education-Conscious Suburban Families",
                "catalyst": "Proven Brand Value Driving Long-Term Family Living"
            },
            {
                "name": "Dr. M.G.R. Educational and Research Institute",
                "distance": "7.7km",
                "time": "22 mins",
                "image": "https://images.unsplash.com/photo-1525921429624-479b6a26d84d?auto=format&fit=crop&w=1000&q=80",
                "importance": "Major Deemed University offering multidisciplinary engineering, dental, and medical programs anchoring thousands of staff and students.",
                "demographic": "University Staff, Professors & Students",
                "catalyst": "Substantial Higher Education Workforce Presence"
            }
        ]
    },
    {
        "id": "hospitals",
        "name": "Hospitals & Healthcare",
        "count": 6,
        "color": "#DC2626",
        "sub": "Immediate healthcare corridor along Poonamallee High Road backed by quaternary hospitals",
        "items": [
            {
                "name": "Aravind Eye Hospital (Poonamallee High Rd)",
                "distance": "1.3km",
                "time": "2 mins",
                "image": "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&w=1000&q=80",
                "importance": "State-of-the-art super-specialty eye care hospital providing world-class ophthalmology services just 2 minutes away.",
                "demographic": "Neighborhood Residents & Senior Citizens",
                "catalyst": "Super-Specialty Eye Care at the Project's Doorstep"
            },
            {
                "name": "ACS Medical College Hospital",
                "distance": "1.7km",
                "time": "3 mins",
                "image": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=1000&q=80",
                "importance": "Large-scale teaching hospital providing 24/7 emergency trauma, outpatient, and multi-specialty inpatient healthcare within 3 minutes.",
                "demographic": "Families Seeking Instant Medical Emergency Access",
                "catalyst": "Round-the-Clock Emergency Medical Security"
            },
            {
                "name": "Sri Ramachandra Medical Centre (SRMC, Porur)",
                "distance": "4.3km",
                "time": "14 mins",
                "image": "https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=1000&q=80",
                "importance": "1,800-bed world-renowned quaternary care hospital with international accreditations, 24/7 trauma, and organ transplant departments.",
                "demographic": "Demanding Homebuyers Seeking Premier Medical Safety",
                "catalyst": "Premier Healthcare Anchor within a 15-Minute Radius"
            },
            {
                "name": "Saveetha Dental Hospital & Healthcare",
                "distance": "4.3km",
                "time": "9 mins",
                "image": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=1000&q=80",
                "importance": "Premier healthcare facility known for specialized maxillo-facial, oral health, and general healthcare operations.",
                "demographic": "Specialized Dental & Health Care Seekers",
                "catalyst": "Specialized Healthcare Institutional Support"
            },
            {
                "name": "Apollo Speciality Hospital (Vanagaram)",
                "distance": "5.6km",
                "time": "14 mins",
                "image": "https://images.unsplash.com/photo-1587351021759-3e566b6af7cc?auto=format&fit=crop&w=1000&q=80",
                "importance": "Flagship Apollo tertiary hospital easily reached via Chennai Bypass, featuring advanced cardiology, oncology, and 24/7 critical emergency care.",
                "demographic": "High-Income Families Trusting Leading Private Healthcare",
                "catalyst": "Gold-Standard Super-Specialty Medical Reassurance"
            },
            {
                "name": "MIOT International Hospital (Manapakkam)",
                "distance": "9.1km",
                "time": "24 mins",
                "image": "https://images.unsplash.com/photo-1538108149393-fbbd81895907?auto=format&fit=crop&w=1000&q=80",
                "importance": "World-class orthopedic and multi-organ transplant hospital attracting international patients, medical tourists, and senior healthcare staff.",
                "demographic": "Senior Doctors, Healthcare Executives & Expats",
                "catalyst": "High-Income Healthcare Workforce Seeking Quality Homes"
            }
        ]
    },
    {
        "id": "entertainment",
        "name": "Entertainment, Retail & Culture",
        "count": 6,
        "color": "#9333EA",
        "sub": "Sacred cultural pilgrimage landmarks, mega hypermarkets, and destination malls",
        "items": [
            {
                "name": "Arulmigu Devi Karumariamman Temple (Thiruverkadu)",
                "distance": "4.2km",
                "time": "11 mins",
                "image": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1000&q=80",
                "importance": "Famed state-wide pilgrimage shrine drawing millions annually; infuses the entire micro-market with rich cultural heritage, peace, and spiritual prestige.",
                "demographic": "Devout Homebuyers, Multi-Generational Families & Retirees",
                "catalyst": "Permanent Cultural & Spiritual Heritage Value Anchor"
            },
            {
                "name": "Super Saravana Stores (Porur)",
                "distance": "6.3km",
                "time": "17 mins",
                "image": "https://images.unsplash.com/photo-1555529669-e69e7aa0ba9a?auto=format&fit=crop&w=1000&q=80",
                "importance": "Massive multi-storey hypermarket fulfilling all gold, apparel, grocery, and home goods shopping under one roof.",
                "demographic": "Families Seeking Comprehensive Household Shopping",
                "catalyst": "Unmatched Daily & Festival Retail Convenience"
            },
            {
                "name": "Rohini Silver Screens (Koyambedu)",
                "distance": "9.6km",
                "time": "29 mins",
                "image": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=1000&q=80",
                "importance": "Iconic cinema entertainment complex with state-of-the-art Dolby Atmos projection, popular for weekend family movie outings.",
                "demographic": "Youth, Young Couples & Moviegoers",
                "catalyst": "Celebrated Weekend Entertainment Destination"
            },
            {
                "name": "EVP Cinemas / EVP World",
                "distance": "10.1km",
                "time": "15 mins",
                "image": "https://images.unsplash.com/photo-1517649763962-0c623266ddc0?auto=format&fit=crop&w=1000&q=80",
                "importance": "Large leisure, cinema, and entertainment complex situated along the western Bangalore highway corridor.",
                "demographic": "Families, Film Enthusiasts & Weekend Travelers",
                "catalyst": "Western Highway Leisure & Recreation Destination"
            },
            {
                "name": "VR Chennai (Anna Nagar / Koyambedu)",
                "distance": "10.5km",
                "time": "32 mins",
                "image": "https://images.unsplash.com/photo-1567449303078-57ad995bd301?auto=format&fit=crop&w=1000&q=80",
                "importance": "Award-winning flagship lifestyle shopping mall featuring luxury international brands, PVR P[XL] multiplex, and gourmet dining.",
                "demographic": "Cosmopolitan Luxury Shoppers & High-Income Buyers",
                "catalyst": "Direct Link to Chennai's Premier Lifestyle Destination"
            },
            {
                "name": "Nexus Vijaya Mall (Vadapalani)",
                "distance": "12.6km",
                "time": "36 mins",
                "image": "https://images.unsplash.com/photo-1519567241046-7f570eee3ce6?auto=format&fit=crop&w=1000&q=80",
                "importance": "Flagship central shopping mall featuring international fashion retail, IMAX screens, and extensive food courts.",
                "demographic": "Discerning Urban Shoppers & Cinephiles",
                "catalyst": "Complete Metropolitan Shopping & Entertainment Access"
            }
        ]
    },
    {
        "id": "transit",
        "name": "Connectivity & Transit Hubs",
        "count": 11,
        "color": "#0D9488",
        "sub": "Strategic junction connecting Poonamallee High Road, Chennai Bypass, and Metro Phase 2",
        "items": [
            {
                "name": "Velappanchavadi Bus Stop (Poonamallee High Rd)",
                "distance": "650m (walk) / 2.9km (bike)",
                "time": "6 mins",
                "image": "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?auto=format&fit=crop&w=1000&q=80",
                "importance": "Immediate walkable bus stop (650m pedestrian access / 2.9km road) connecting MTC buses directly along Poonamallee High Road.",
                "demographic": "Daily Commuters, Students & Domestic Staff",
                "catalyst": "Walkable Arterial Transit on NH-48"
            },
            {
                "name": "Maduravoyal Metro Station (Phase 2)",
                "distance": "1.6km",
                "time": "5 mins",
                "image": "https://images.unsplash.com/photo-1517649763962-0c623266ddc0?auto=format&fit=crop&w=1000&q=80",
                "importance": "Nearest upcoming Chennai Metro Phase 2 station on Corridor 4. Slashes travel time to Central Chennai down to 20 minutes.",
                "demographic": "IT Professionals & Daily Central City Commuters",
                "catalyst": "Prime Metro Catalyst: 35%–45% Capital Value Appreciation"
            },
            {
                "name": "Kumananchavadi Metro Station (Phase 2)",
                "distance": "2.6km",
                "time": "5 mins",
                "image": "https://images.unsplash.com/photo-1474487548417-781cb71495f3?auto=format&fit=crop&w=1000&q=80",
                "importance": "Key upcoming Phase 2 Metro station facilitating seamless westbound and eastbound connectivity along Corridor 4.",
                "demographic": "Corporate Commuters towards Poonamallee & Vadapalani",
                "catalyst": "Dual-Station Metro Advantage Driving Fast Pre-sales"
            },
            {
                "name": "Thiruverkadu Bus Terminus",
                "distance": "4.0km",
                "time": "9 mins",
                "image": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1000&q=80",
                "importance": "Major local bus depot providing direct bus routes across Chennai to Broadway, Tambaram, Central, and Guindy.",
                "demographic": "Public Transit Commuters & Local Residents",
                "catalyst": "Comprehensive Suburban Bus Network"
            },
            {
                "name": "Poonamallee Bus Terminus",
                "distance": "4.8km",
                "time": "9 mins",
                "image": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1000&q=80",
                "importance": "Massive western multimodal transport hub connecting intra-city buses and mofussil services towards Bangalore highway.",
                "demographic": "Intercity Travelers & Regional Commuters",
                "catalyst": "Western Regional Transit Hub Anchor"
            },
            {
                "name": "Porur Junction Metro Station (Phase 2)",
                "distance": "5.5km",
                "time": "17 mins",
                "image": "https://images.unsplash.com/photo-1517649763962-0c623266ddc0?auto=format&fit=crop&w=1000&q=80",
                "importance": "Crucial strategic double-corridor interchange connecting Corridor 4 and Corridor 5 (Madhavaram to Sholinganallur).",
                "demographic": "Techies Commuting across Porur, Guindy & OMR",
                "catalyst": "Interchange Station: Highest Property Value Appreciation"
            },
            {
                "name": "Vanagaram Toll Plaza / Chennai Bypass (NH-32)",
                "distance": "5.9km",
                "time": "16 mins",
                "image": "https://images.unsplash.com/photo-1502877338535-766e1452684a?auto=format&fit=crop&w=1000&q=80",
                "importance": "Direct high-speed expressway access linking NH-32 and NH-48 towards Sriperumbudur, Ambattur, and GST Road.",
                "demographic": "Industrial & Manufacturing Corporate Leaders",
                "catalyst": "Seamless Bypass Mobility Avoiding City Bottlenecks"
            },
            {
                "name": "Chennai - Maduravoyal Bypass (W)",
                "distance": "6.3km",
                "time": "16 mins",
                "image": "https://images.unsplash.com/photo-1502877338535-766e1452684a?auto=format&fit=crop&w=1000&q=80",
                "importance": "Vital western bypass corridor connecting the upcoming double-decker elevated port expressway to Chennai Port and NH-48.",
                "demographic": "Commercial Investors & Freight Logistics Leaders",
                "catalyst": "Port Expressway Infrastructure Appreciation Multiplier"
            },
            {
                "name": "Avadi Railway Station (Suburban Rail)",
                "distance": "9.7km",
                "time": "22 mins",
                "image": "https://images.unsplash.com/photo-1474487548417-781cb71495f3?auto=format&fit=crop&w=1000&q=80",
                "importance": "Major suburban rail junction connecting directly to Chennai Central, Arakkonam, and Thiruvallur along the western line.",
                "demographic": "Heavy Suburban Rail Commuters",
                "catalyst": "Multimodal Rail Backup Complementing Metro Network"
            },
            {
                "name": "Koyambedu Metro & CMBT Bus Terminus",
                "distance": "11.4km",
                "time": "31 mins",
                "image": "https://images.unsplash.com/photo-1517649763962-0c623266ddc0?auto=format&fit=crop&w=1000&q=80",
                "importance": "Chennai's primary operational metro interchange (Green & Blue line links) and regional bus transport headquarters.",
                "demographic": "All Metropolitan Commuters & Regional Travelers",
                "catalyst": "Direct Access to Chennai's Core Transit Interchange"
            },
            {
                "name": "Chennai International Airport (MAA)",
                "distance": "16.6km",
                "time": "39 mins",
                "image": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1000&q=80",
                "importance": "Reachable via Chennai Bypass / Pallavaram road in ~39 minutes, providing seamless connectivity for corporate frequent flyers and NRIs.",
                "demographic": "NRIs, Corporate Executives & Frequent Business Flyers",
                "catalyst": "Air Transit Accessibility: Critical Selling Hook for Gated Enclaves"
            }
        ]
    }
]

# Generate static tabs & panels
tab_buttons_html = ""
tab_contents_html = ""

for t_idx, cat in enumerate(noombal_data):
    is_active = "active" if t_idx == 0 else ""
    display_style = "block" if t_idx == 0 else "none"

    tab_buttons_html += f'''
    <button class="stab-btn {is_active}" onclick="selectCategory('{cat['id']}', this)">
        <span class="tab-dot" style="background-color: {cat['color']};"></span>
        <span>{cat['name']}</span>
        <span class="stab-count">{cat['count']}</span>
    </button>
    '''

    items_list_html = ""
    for idx, item in enumerate(cat['items']):
        item_active = "active" if idx == 0 else ""
        items_list_html += f'''
        <li class="poi-item {item_active}" id="{cat['id']}-li-{idx}" onclick="showDetail('{cat['id']}', {idx})">
            <div class="poi-header">
                <div class="poi-title-wrap">
                    <span class="poi-idx">{idx+1:02d}.</span>
                    <span class="poi-name">{item['name']}</span>
                </div>
                <div class="poi-time-wrap">
                    <span class="poi-dist">{item['distance']}</span>
                    <span class="poi-time">({item['time']})</span>
                </div>
            </div>
        </li>
        '''

    first = cat['items'][0]
    tab_contents_html += f'''
    <div class="cat-content-panel" id="panel-{cat['id']}" style="display: {display_style};">
        <div class="panel-layout">
            
            <!-- Left Side: Landmarks List -->
            <div class="panel-left">
                <div class="col-header-box">
                    <h2 class="col-title" style="color: {cat['color']};">{cat['name']} ({cat['count']})</h2>
                    <p class="col-sub">{cat['sub']}</p>
                </div>
                <ul class="list-container">
                    {items_list_html}
                </ul>
            </div>

            <!-- Right Side: Rich Visual & Real Estate Importance Card -->
            <div class="panel-right">
                <div class="detail-card-container">
                    
                    <!-- Landmark Image Banner -->
                    <div class="photo-banner-wrap">
                        <img id="{cat['id']}-img" class="photo-banner" src="{first['image']}" alt="{first['name']}">
                        <div class="photo-overlay">
                            <span class="distance-pill" id="{cat['id']}-dist-badge">{first['distance']} • {first['time']} from Site</span>
                        </div>
                    </div>

                    <!-- Landmark Name & Category -->
                    <div class="detail-header-block">
                        <div class="detail-cat-tag" style="color: {cat['color']};">{cat['name'].upper()}</div>
                        <h3 class="detail-landmark-title" id="{cat['id']}-title">{first['name']}</h3>
                    </div>

                    <!-- Strategic Importance Section -->
                    <div class="importance-highlight-box">
                        <div class="ih-label">Real Estate Importance & Strategic Advantage</div>
                        <p class="ih-text" id="{cat['id']}-desc">{first['importance']}</p>
                    </div>

                    <!-- 2-Column Metrics / Target Market Breakdown -->
                    <div class="metrics-grid">
                        <div class="metric-sub-card">
                            <div class="m-label">Target Buyer Demographics</div>
                            <div class="m-val" id="{cat['id']}-demographic">{first['demographic']}</div>
                        </div>
                        <div class="metric-sub-card">
                            <div class="m-label">Investment / Yield Driver</div>
                            <div class="m-val" id="{cat['id']}-catalyst">{first['catalyst']}</div>
                        </div>
                    </div>

                </div>
            </div>

        </div>
    </div>
    '''

full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Appraisal Slide: Location Highlights (Noombal Pin)</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: #0B0F19;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            color: #0F172A;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}

        /* 16:9 Internal Presentation Slide Canvas */
        .slide-canvas {{
            width: 100%;
            max-width: 1400px;
            aspect-ratio: 16 / 9;
            background: #FFFFFF;
            border-radius: 12px;
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.8);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            border: 1px solid #1E293B;
        }}

        /* Slide Top Header Bar */
        .slide-header {{
            padding: 16px 36px 12px;
            background: #FFFFFF;
            border-bottom: 1px solid #E2E8F0;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .header-left {{
            display: flex;
            flex-direction: column;
            gap: 2px;
        }}

        .tagline {{
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.5px;
            color: #0F766E;
            text-transform: uppercase;
        }}

        .slide-title {{
            font-size: 23px;
            font-weight: 700;
            color: #0F172A;
            letter-spacing: -0.3px;
        }}

        .header-right {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .coord-pill {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #F1F5F9;
            border: 1px solid #CBD5E1;
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            color: #334155;
            font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
        }}

        .coord-dot {{
            width: 8px;
            height: 8px;
            background: #10B981;
            border-radius: 50%;
        }}

        /* Category Selector Buttons */
        .slide-tabs-nav {{
            padding: 9px 36px;
            background: #F8FAFC;
            border-bottom: 1px solid #E2E8F0;
            display: flex;
            align-items: center;
            gap: 10px;
            overflow-x: auto;
        }}

        .stab-btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 7px 16px;
            background: #FFFFFF;
            border: 1px solid #CBD5E1;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 600;
            color: #475569;
            cursor: pointer;
            transition: all 0.15s ease;
            white-space: nowrap;
        }}

        .stab-btn:hover {{
            background: #F1F5F9;
            color: #0F172A;
            border-color: #94A3B8;
        }}

        .stab-btn.active {{
            background: #0F172A;
            color: #FFFFFF;
            border-color: #0F172A;
        }}

        .tab-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
        }}

        .stab-count {{
            background: rgba(0, 0, 0, 0.08);
            padding: 1px 6px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
        }}

        .stab-btn.active .stab-count {{
            background: rgba(255, 255, 255, 0.2);
            color: #FFFFFF;
        }}

        /* Main Body Panels */
        .slide-main-body {{
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            background: #FFFFFF;
        }}

        .cat-content-panel {{
            height: 100%;
            display: flex;
            flex-direction: column;
        }}

        .panel-layout {{
            height: 100%;
            display: grid;
            grid-template-columns: 46% 54%;
            overflow: hidden;
        }}

        /* Left Side: Proximity List */
        .panel-left {{
            padding: 20px 24px 18px 36px;
            display: flex;
            flex-direction: column;
            border-right: 1px solid #E2E8F0;
            overflow-y: auto;
        }}

        .col-header-box {{
            margin-bottom: 12px;
        }}

        .col-title {{
            font-size: 17px;
            font-weight: 700;
            margin-bottom: 3px;
        }}

        .col-sub {{
            font-size: 12.5px;
            color: #64748B;
        }}

        .list-container {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 7px;
            overflow-y: auto;
            flex-grow: 1;
            padding-right: 6px;
        }}

        .list-container::-webkit-scrollbar {{
            width: 5px;
        }}
        .list-container::-webkit-scrollbar-thumb {{
            background: #CBD5E1;
            border-radius: 4px;
        }}

        .poi-item {{
            padding: 9px 12px;
            border-radius: 6px;
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            cursor: pointer;
            transition: all 0.15s ease;
        }}

        .poi-item:hover, .poi-item.active {{
            background: #F1F5F9;
            border-color: #0F172A;
            transform: translateX(4px);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
        }}

        .poi-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
        }}

        .poi-title-wrap {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 13.5px;
            font-weight: 600;
            color: #0F172A;
            line-height: 1.3;
        }}

        .poi-idx {{
            font-size: 12px;
            font-weight: 700;
            color: #94A3B8;
            min-width: 20px;
        }}

        .poi-time-wrap {{
            display: flex;
            align-items: center;
            gap: 4px;
            white-space: nowrap;
        }}

        .poi-dist {{
            font-size: 12.5px;
            font-weight: 700;
            color: #0F172A;
        }}

        .poi-time {{
            font-size: 11.5px;
            font-weight: 600;
            color: #64748B;
        }}

        .poi-item.active .poi-dist {{
            color: #0F766E;
        }}

        /* Right Side: Visual & Real Estate Importance Card */
        .panel-right {{
            padding: 20px 36px 18px 24px;
            background: #F8FAFC;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
        }}

        .detail-card-container {{
            background: #FFFFFF;
            border-radius: 8px;
            border: 1px solid #E2E8F0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            height: 100%;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
            justify-content: space-between;
        }}

        .photo-banner-wrap {{
            position: relative;
            width: 100%;
            height: 200px;
            border-radius: 6px;
            overflow: hidden;
            margin-bottom: 14px;
            background: #E2E8F0;
        }}

        .photo-banner {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }}

        .photo-overlay {{
            position: absolute;
            top: 12px;
            right: 12px;
        }}

        .distance-pill {{
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(4px);
            color: #FFFFFF;
            font-size: 12px;
            font-weight: 700;
            padding: 5px 12px;
            border-radius: 4px;
            letter-spacing: 0.5px;
        }}

        .detail-header-block {{
            margin-bottom: 12px;
        }}

        .detail-cat-tag {{
            font-size: 10.5px;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 2px;
        }}

        .detail-landmark-title {{
            font-size: 20px;
            font-weight: 700;
            color: #0F172A;
            line-height: 1.25;
        }}

        .importance-highlight-box {{
            background: #F8FAFC;
            border-left: 3px solid #0F766E;
            padding: 12px 16px;
            border-radius: 4px;
            margin-bottom: 14px;
        }}

        .ih-label {{
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #0F766E;
            margin-bottom: 4px;
        }}

        .ih-text {{
            font-size: 13px;
            color: #334155;
            line-height: 1.5;
        }}

        .metrics-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }}

        .metric-sub-card {{
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            padding: 10px 14px;
            border-radius: 6px;
        }}

        .m-label {{
            font-size: 10.5px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #64748B;
            margin-bottom: 3px;
        }}

        .m-val {{
            font-size: 12.5px;
            font-weight: 600;
            color: #0F172A;
            line-height: 1.35;
        }}

        /* Slide Bottom Bar */
        .slide-footer {{
            padding: 10px 36px;
            background: #FFFFFF;
            border-top: 1px solid #E2E8F0;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 11.5px;
            color: #64748B;
        }}

        .status-badge {{
            background: #F1F5F9;
            border: 1px solid #CBD5E1;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 600;
            color: #334155;
        }}

        @media (max-width: 1024px) {{
            .slide-canvas {{
                aspect-ratio: auto;
                min-height: 95vh;
            }}
            .panel-layout {{
                grid-template-columns: 1fr;
            }}
            .panel-right {{
                height: auto;
            }}
        }}
    </style>
</head>
<body>

    <!-- Executive Slide Canvas -->
    <div class="slide-canvas">
        
        <!-- Slide Top Bar -->
        <div class="slide-header">
            <div class="header-left">
                <span class="tagline">Land Acquisition Appraisal • Proximity Analysis</span>
                <h1 class="slide-title">Location Highlights & Micro-Market Proximity (Noombal Pin)</h1>
            </div>
            <div class="header-right">
                <div class="coord-pill">
                    <span class="coord-dot"></span>
                    <span>13°03'33.6"N 80°08'00.0"E (Noombal / Velappanchavadi)</span>
                </div>
            </div>
        </div>

        <!-- Category Selector Buttons -->
        <div class="slide-tabs-nav">
            {tab_buttons_html}
        </div>

        <!-- Slide Body (All 5 Panels Pre-rendered) -->
        <div class="slide-main-body">
            {tab_contents_html}
        </div>

        <!-- Slide Footer Bar -->
        <div class="slide-footer">
            <span>Confidential Internal Evaluation Slide • Verified Landmark Proximities & Drive Times</span>
            <span class="status-badge">Noombal Site Appraisal</span>
        </div>

    </div>

    <!-- Pure Vanilla JS for Instant Tab Switching and Item Selection -->
    <script>
        const appData = {json.dumps(noombal_data)};

        function selectCategory(catId, btnEl) {{
            // Hide all panels
            document.querySelectorAll('.cat-content-panel').forEach(p => p.style.display = 'none');
            // Show target panel
            const panel = document.getElementById('panel-' + catId);
            if (panel) panel.style.display = 'block';

            // Update tab button styles
            document.querySelectorAll('.stab-btn').forEach(b => b.classList.remove('active'));
            if (btnEl) btnEl.classList.add('active');
        }}

        function showDetail(catId, index) {{
            const catObj = appData.find(c => c.id === catId);
            if (!catObj || !catObj.items[index]) return;

            const item = catObj.items[index];

            // Highlight list item
            const panel = document.getElementById('panel-' + catId);
            if (panel) {{
                panel.querySelectorAll('.poi-item').forEach((li, idx) => {{
                    if (idx === index) li.classList.add('active');
                    else li.classList.remove('active');
                }});
            }}

            // Update photo & detail elements
            const imgEl = document.getElementById(catId + '-img');
            const distBadge = document.getElementById(catId + '-dist-badge');
            const titleEl = document.getElementById(catId + '-title');
            const descEl = document.getElementById(catId + '-desc');
            const demoEl = document.getElementById(catId + '-demographic');
            const catEl = document.getElementById(catId + '-catalyst');

            if (imgEl) imgEl.src = item.image;
            if (distBadge) distBadge.innerText = item.distance + ' • ' + item.time + ' from Site';
            if (titleEl) titleEl.innerText = item.name;
            if (descEl) descEl.innerText = item.importance;
            if (demoEl) demoEl.innerText = item.demographic;
            if (catEl) catEl.innerText = item.catalyst;
        }}
    </script>
</body>
</html>
'''

with open('/Users/elan/mangadu-tvs-emerald-presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Successfully generated Noombal slide in /Users/elan/mangadu-tvs-emerald-presentation/index.html")
