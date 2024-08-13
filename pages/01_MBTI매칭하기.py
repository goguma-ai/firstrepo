import streamlit as st

# 제목 설정
st.title('🔮 나의 MBTI 궁합 진단기 🔮')

# MBTI 유형 선택
mbti = st.selectbox(
    '당신의 MBTI 유형을 선택하세요:',
    [
        '선택하세요', 'ISTJ', 'ISFJ', 'INFJ', 'INTJ',
        'ISTP', 'ISFP', 'INFP', 'INTP',
        'ESTP', 'ESFP', 'ENFP', 'ENTP',
        'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
    ]
)

# 버튼을 눌렀을 때 특성 및 궁합 출력
if st.button('✨ 나의 특성 및 궁합 보기 ✨'):
    if mbti != '선택하세요':
        # MBTI 유형에 따른 특성 및 궁합
        mbti_info = {
            'ISTJ': {
                'description': '📈 신뢰할 수 있고 책임감이 강한 ISTJ! 당신은 꼼꼼하고 조직적인 성격으로, 계획을 세우고 실천하는 데 능숙해요.',
                'best_match': 'ESFP 🎉 (균형을 맞추고 즐거움을 더해주는 관계)',
                'worst_match': 'ENFP 🌪️ (예측 불가능한 변화를 추구하는 관계)'
            },
            'ISFJ': {
                'description': '🛡️ 세심하고 헌신적인 ISFJ! 당신은 타인을 돕고 지원하는 것을 중요하게 여기며, 매우 따뜻한 마음을 가지고 있어요.',
                'best_match': 'ESTP 🏎️ (활기차고 실용적인 관계)',
                'worst_match': 'ENTP 🌩️ (도전적이고 논쟁을 즐기는 관계)'
            },
            'INFJ': {
                'description': '🧙‍♂️ 직관적이고 통찰력 있는 INFJ! 당신은 깊은 이해와 연민을 바탕으로 사람들과의 관계를 형성하며, 의미 있는 삶을 추구해요.',
                'best_match': 'ENFP 🌟 (창의적이고 활기찬 관계)',
                'worst_match': 'ESTP 🏎️ (즉흥적이고 모험을 즐기는 관계)'
            },
            'INTJ': {
                'description': '🧠 분석적이고 전략적인 INTJ! 당신은 큰 그림을 보는 능력이 뛰어나며, 복잡한 문제를 해결하는 데 능숙해요.',
                'best_match': 'ENFP 🌟 (창의적이고 열정적인 관계)',
                'worst_match': 'ESFP 🎤 (즉흥적이고 감각적인 관계)'
            },
            'ISTP': {
                'description': '🛠️ 실용적이고 문제 해결을 좋아하는 ISTP! 당신은 손재주가 좋고, 도전적인 상황을 즐겨요.',
                'best_match': 'ESFJ 🎈 (따뜻하고 사교적인 관계)',
                'worst_match': 'ENFJ 🌍 (강한 주장을 펼치는 관계)'
            },
            'ISFP': {
                'description': '🎨 감성적이고 예술적인 ISFP! 당신은 개인적인 가치와 미적 감각을 중요하게 여기며, 자유로운 영혼을 가졌어요.',
                'best_match': 'ESTJ 🧩 (구조적이고 실용적인 관계)',
                'worst_match': 'ENTJ 🏢 (지배적이고 목표 지향적인 관계)'
            },
            'INFP': {
                'description': '🌱 이상적이고 공감능력이 뛰어난 INFP! 당신은 깊은 내면의 가치와 신념을 중요하게 여기며, 사람들에게 큰 감동을 줘요.',
                'best_match': 'ENFJ 🌍 (조화를 이루며 성장하는 관계)',
                'worst_match': 'ESTJ 🧩 (현실적이고 규칙을 중시하는 관계)'
            },
            'INTP': {
                'description': '🔍 논리적이고 탐구적인 INTP! 당신은 독창적인 사고를 통해 새로운 아이디어를 탐구하는 것을 좋아해요.',
                'best_match': 'ENTJ 🏢 (전략적이고 목표 지향적인 관계)',
                'worst_match': 'ESFJ 🎈 (정서적이고 사교적인 관계)'
            },
            'ESTP': {
                'description': '🏎️ 모험적이고 에너지가 넘치는 ESTP! 당신은 현재의 순간을 즐기며, 즉흥적인 결정을 내리는 것을 두려워하지 않아요.',
                'best_match': 'ISFJ 🛡️ (안정적이고 배려심 있는 관계)',
                'worst_match': 'INFJ 🧙‍♂️ (심오하고 사색적인 관계)'
            },
            'ESFP': {
                'description': '🎤 활발하고 사교적인 ESFP! 당신은 사람들과의 교류를 즐기고, 현재의 순간을 즐기며 사는 것을 선호해요.',
                'best_match': 'ISTJ 📈 (안정적이고 신뢰할 수 있는 관계)',
                'worst_match': 'INTJ 🧠 (분석적이고 계획적인 관계)'
            },
            'ENFP': {
                'description': '🌟 열정적이고 창의적인 ENFP! 당신은 항상 새로운 아이디어로 가득 차 있어요. 사람들과의 소통을 즐기고, 세상을 긍정적으로 바라보는 경향이 있어요.',
                'best_match': 'INFJ 🧘‍♂️ (깊은 이해와 조화를 이루는 관계)',
                'worst_match': 'ISTJ 📊 (구조와 규칙을 중시하는 관계)'
            },
            'ENTP': {
                'description': '⚡ 도전적이고 창의적인 ENTP! 당신은 논쟁을 즐기고, 새로운 아이디어를 탐구하며, 혁신적인 접근 방식을 선호해요.',
                'best_match': 'INFJ 🧘‍♂️ (깊이 있는 대화를 나누는 관계)',
                'worst_match': 'ISFJ 🛡️ (전통적이고 안정적인 관계)'
            },
            'ESTJ': {
                'description': '📊 실용적이고 조직적인 ESTJ! 당신은 체계적이고 효율적인 것을 중요하게 여기며, 리더십을 발휘하는 데 능숙해요.',
                'best_match': 'ISFP 🎨 (감성적이고 예술적인 관계)',
                'worst_match': 'INFP 🌱 (이상적이고 감정적인 관계)'
            },
            'ESFJ': {
                'description': '🎈 따뜻하고 사교적인 ESFJ! 당신은 다른 사람들을 돌보는 것을 즐기며, 커뮤니티의 중심에서 활약해요.',
                'best_match': 'ISTP 🛠️ (실용적이고 독립적인 관계)',
                'worst_match': 'INTP 🔍 (논리적이고 탐구적인 관계)'
            },
            'ENFJ': {
                'description': '🌍 배려심이 깊고 카리스마 있는 ENFJ! 당신은 사람들의 성장을 돕고, 주변 사람들과의 조화를 이루는 것을 중요하게 생각해요.',
                'best_match': 'INFP 🌱 (깊은 공감을 나누는 관계)',
                'worst_match': 'ISTP 🛠️ (독립적이고 실용적인 관계)'
            },
            'ENTJ': {
                'description': '🏢 목표 지향적이고 리더십이 뛰어난 ENTJ! 당신은 체계적이고 효율적인 방법으로 목표를 달성하는 것을 중요하게 생각해요.',
                'best_match': 'INTP 🔍 (논리적이고 전략적인 관계)',
                'worst_match': 'ISFP 🎨 (감성적이고 예술적인 관계)'
            },
        }

        if mbti in mbti_info:
            st.write(mbti_info[mbti]['description'])
            st.write(f"💖 가장 잘 맞는 유형: {mbti_info[mbti]['best_match']}")
            st.write(f"💔 가장 맞지 않는 유형: {mbti_info[mbti]['worst_match']}")
        else:
            st.write("🙈 오류가 발생했습니다. 다시 시도해 주세요!")
    else:
        st.write("✍️ MBTI 유형을 선택해 주세요!")

# 주석: 사용자는 자신의 MBTI 유형을 선택하고 재미있는 특성과 궁합을 확인할 수 있습니다.
