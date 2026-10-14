import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 따뜻한 크림/노란색 톤 커스텀 CSS 적용
st.markdown("""
    <style>
    /* 전체 배경색 및 폰트 설정 */
    .stApp {
        background-color: #FFFDF0;
        font-family: 'Pretendard', 'Malgun Gothic', sans-serif;
        color: #4A3E3D;
    }
    
    /* 카드 컨테이너 스타일링 */
    .pokemon-card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 28px;
        box-shadow: 0 10px 25px rgba(229, 180, 80, 0.2);
        border: 2px solid #FDE68A;
        text-align: center;
        margin-top: 15px;
    }

    /* 주요 제목 스타일 */
    .main-title {
        color: #D97706;
        font-weight: 800;
        text-align: center;
        font-size: 2.2rem;
        margin-bottom: 5px;
    }

    .sub-title {
        color: #78350F;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }

    /* 포켓몬 이름 */
    .pokemon-name {
        color: #B45309;
        font-size: 2rem;
        font-weight: 800;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    /* 포켓몬 영문 이름 */
    .pokemon-en-name {
        color: #9CA3AF;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 15px;
    }

    /* 정보 뱃지 (타입 & 특징) */
    .info-badge {
        display: inline-block;
        background-color: #FEF3C7;
        color: #92400E;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.95rem;
        margin: 4px;
    }

    /* 이유 설명 상자 */
    .reason-box {
        background-color: #FFFBEB;
        border-left: 5px solid #F59E0B;
        padding: 15px 18px;
        border-radius: 8px;
        text-align: left;
        margin-top: 20px;
        font-size: 1.05rem;
        line-height: 1.6;
        color: #451A03;
    }

    /* 라디오 버튼 스타일 수정 */
    div[data-testid="stMarkdownContainer"] > p {
        font-size: 1.1rem !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 16가지 MBTI 포켓몬 데이터베이스
POKEMON_DATA = {
    "ISTJ": {
        "ko_name": "거북왕",
        "en_name": "Blastoise",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "type": "물 (Water)",
        "trait": "신중함 / 철저함 / 책임감",
        "reason": "규칙과 질서를 중시하며 언제나 묵묵하게 자신의 책임을 다하는 거북왕은 신중하고 철저한 ISTJ의 든든한 조력자입니다."
    },
    "ISFJ": {
        "ko_name": "해피너스",
        "en_name": "Blissey",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "type": "노말 (Normal)",
        "trait": "헌신적 / 헌신과 배려 / 따뜻함",
        "reason": "상처받은 이를 정성껏 돌보는 해피너스는 주변 사람들의 필요를 먼저 챙기고 배려하는 ISFJ의 온화한 마음과 완벽히 닮았습니다."
    },
    "INFJ": {
        "ko_name": "뮤",
        "en_name": "Mew",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png",
        "type": "에스퍼 (Psychic)",
        "trait": "신비로움 / 통찰력 / 이상주의",
        "reason": "깊은 통찰력과 신비로운 기운을 지닌 뮤는 세상을 더 깊게 이해하고자 노력하는 INFJ의 이상적인 단짝입니다."
    },
    "INTJ": {
        "ko_name": "후딘",
        "en_name": "Alakazam",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
        "type": "에스퍼 (Psychic)",
        "trait": "뛰어난 지능 / 전략가 / 냉철함",
        "reason": "IQ 5000을 자랑하는 절대적 지능의 후딘은 문제의 본질을 파악하고 논리적 전략을 세우는 INTJ와 조화를 이룹니다."
    },
    "ISTP": {
        "ko_name": "개굴닌자",
        "en_name": "Greninja",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/658.png",
        "type": "물 / 악 (Water / Dark)",
        "trait": "냉철함 / 침착함 / 문제 해결",
        "reason": "조용하지만 순간의 기지를 발휘해 상황을 해결하는 개굴닌자는 순발력과 도구 활용에 강한 ISTP와 정밀한 호흡을 과시합니다."
    },
    "ISFP": {
        "ko_name": "이브이",
        "en_name": "Eevee",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "type": "노말 (Normal)",
        "trait": "유연성 / 예술적 감각 / 다재다능",
        "reason": "어떤 모습으로든 피어날 가능성을 품은 이브이는 자유롭고 조용한 감성을 소중히 여기는 ISFP에게 마음의 위안이 되어 줍니다."
    },
    "INFP": {
        "ko_name": "가가멜아닌 가디안",
        "en_name": "Gardevoir",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png",
        "type": "초능력 / 페어리 (Psychic / Fairy)",
        "trait": "풍부한 공감 / 순수한 마음 / 수호자",
        "reason": "트레이너의 마음을 예리하게 느끼고 목숨 바쳐 지키려는 가디안은 풍부한 감수성을 지닌 INFP의 영혼의 짝꿍입니다."
    },
    "INTP": {
        "ko_name": "로토무",
        "en_name": "Rotom",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/479.png",
        "type": "전기 / 고스트 (Electric / Ghost)",
        "trait": "호기심 / 탐구심 / 창의적",
        "reason": "전자제품을 탐구하고 호기심 넘치는 행동을 즐기는 로토무는 지적 원동력이 끊이지 않는 INTP와 훌륭한 연구 파트너가 됩니다."
    },
    "ESTP": {
        "ko_name": "번치코",
        "en_name": "Blaziken",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/257.png",
        "type": "불꽃 / 격투 (Fire / Fighting)",
        "trait": "열정적 / 스릴 즐김 / 행동파",
        "reason": "강렬한 도전을 두려워하지 않고 직관적으로 몸을 던지는 번치코는 스릴과 역동적인 변화를 좋아하는 ESTP의 에너지를 채워줍니다."
    },
    "ESFP": {
        "ko_name": "푸린",
        "en_name": "Jigglypuff",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "type": "노말 / 페어리 (Normal / Fairy)",
        "trait": "분위기 메이커 / 사교적 / 즐거움",
        "reason": "언제 어디서나 주목받기 좋아하고 사람들에게 노래와 즐거움을 안겨주는 푸린은 사교적이고 밝은 ESFP와 완벽히 상응합니다."
    },
    "ENFP": {
        "ko_name": "피카츄",
        "en_name": "Pikachu",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "type": "전기 (Electric)",
        "trait": "에너지 넘침 / 발랄함 / 창의적",
        "reason": "통통 튀는 스파크처럼 긍정적이고 발랄한 매력을 발산하는 피카츄는 상상력이 풍부하고 매력 넘치는 ENFP의 둘도 없는 단짝입니다."
    },
    "ENTP": {
        "ko_name": "팬텀",
        "en_name": "Gengar",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "type": "고스트 / 독 (Ghost / Poison)",
        "trait": "장난기 넘침 / 독창적 / 재치",
        "reason": "엉뚱하고 재치 있는 장난으로 모두를 깜짝 놀라게 만드는 팬텀은 고정관념을 깨기 좋아하는 ENTP와 흥미진진한 케미를 보여줍니다."
    },
    "ESTJ": {
        "ko_name": "괴력몬",
        "en_name": "Machamp",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/68.png",
        "type": "격투 (Fighting)",
        "trait": "추진력 / 강한 실행력 / 리더십",
        "reason": "탁월한 집행력과 체력으로 목표를 정면으로 돌파해 나가는 괴력몬은 체계적인 추진력을 중시하는 ESTJ의 강력한 동반자입니다."
    },
    "ESFJ": {
        "ko_name": "토게피",
        "en_name": "Togepi",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/175.png",
        "type": "페어리 (Fairy)",
        "trait": "친화력 / 행운의 상징 / 따뜻함",
        "reason": "주변에 밝은 에너지를 퍼뜨리며 사람들을 하나로 모으는 토게피는 따뜻한 리더십과 친화력을 지닌 ESFJ와 잘 어울립니다."
    },
    "ENFJ": {
        "ko_name": "망나뇽",
        "en_name": "Dragonite",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png",
        "type": "드래곤 / 비행 (Dragon / Flying)",
        "trait": "상냥함 / 포용력 / 바다의 구원자",
        "reason": "위기에 처한 이들을 돕기 위해 표류하는 배를 구하는 망나뇽은 사려 깊고 다른 이를 이끄는 ENFJ의 카리스마를 상징합니다."
    },
    "ENTJ": {
        "ko_name": "뮤츠",
        "en_name": "Mewtwo",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "type": "에스퍼 (Psychic)",
        "trait": "압도적 결단력 / 비전 / 야망",
        "reason": "스스로의 힘으로 최고에 오르고 강한 의지와 목표 의식을 증명하는 뮤츠는 비전을 제시하고 이끄는 ENTJ의 카리스마와 맞닿아 있습니다."
    }
}

# 4. 앱 헤더 화면
st.markdown('<div class="main-title">✨ MBTI 단짝 포켓몬 찾기 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">당신의 성격 유형에 딱 맞는 운명의 포켓몬을 찾아보세요!</div>', unsafe_allow_html=True)

# 5. MBTI 선택 셀렉트박스
mbti_list = list(POKEMON_DATA.keys())
selected_mbti = st.selectbox(
    "👉 당신의 MBTI 유형을 선택해 주세요:",
    ["선택하세요..."] + mbti_list,
    index=0
)

# 6. 결과 출력 처리
if selected_mbti != "선택하세요...":
    # 단짝 포켓몬을 찾으면 축하 폭죽 효과 연출
    st.balloons()
    
    data = POKEMON_DATA[selected_mbti]
    
    # 포켓몬 정보 카드 UI 생성
    st.markdown(f"""
        <div class="pokemon-card">
            <div style="font-size: 1.2rem; font-weight: 700; color: #D97706;">
                [{selected_mbti}] 당신의 단짝 포켓몬은?
            </div>
            <div class="pokemon-name">{data['ko_name']}</div>
            <div class="pokemon-en-name">{data['en_name']}</div>
            <img src="{data['img']}" width="250" style="margin: 10px 0;">
            <div>
                <span class="info-badge">타입: {data['type']}</span>
                <span class="info-badge">성향: {data['trait']}</span>
            </div>
            <div class="reason-box">
                💡 <b>함께해야 하는 이유</b><br>
                {data['reason']}
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("💡 위 드롭다운 메뉴에서 MBTI 유형을 고르시면 운명의 포켓몬이 등장합니다!")
