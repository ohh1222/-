import streamlit as st

st.set_page_config(page_title='财务判断室 · 科大讯飞', page_icon='🏢', layout='centered')

ROLES = [
    {'id': 'mgmt',   'icon': '🏢', 'name': '管理层',   'desc': '追求利润稳定，维护融资能力'},
    {'id': 'acct',   'icon': '📊', 'name': '财务人员', 'desc': '执行准则，承受内外双重压力'},
    {'id': 'audit',  'icon': '🔍', 'name': '审计师',   'desc': '核查证据，面对信息不对称'},
    {'id': 'invest', 'icon': '📈', 'name': '投资者',   'desc': '判断利润质量，防范估值风险'},
    {'id': 'reg',    'icon': '⚖️', 'name': '监管者',   'desc': '核查合规，维护市场信息质量'},
    {'id': 'cred',   'icon': '🏦', 'name': '债权人',   'desc': '评估偿债能力，识别资产水分'},
]

SCENES = [
    {
        'year': '2022年底',
        'title': '星火大模型立项，资本化比例决策',
        'desc': '科大讯飞全年研发投入33.55亿元，利润承压（净利润仅5.61亿）。星火大模型正式立项，技术可行性已初步验证，但商业化路径尚不明朗。现在需要决定当年资本化比例。',
        'stats': [
            {'label': '研发总投入', 'value': '33.55亿', 'delta': None},
            {'label': '净利润',     'value': '5.61亿',  'delta': '-63.9% YoY'},
            {'label': '上年资本化率','value': '42.10%', 'delta': None},
        ],
        'lens': {
            'mgmt':  '利润已大幅下滑，若再压低资本化比例，净利润将跌破5亿，影响高管薪酬考核和定增资质。',
            'acct':  '准则要求逐项目判断，但管理层已明示"不能让利润太难看"。星火大模型商业化路径不清晰，资本化依据存疑。',
            'audit': '需核查星火大模型是否满足五项资本化条件，但技术验证文件由管理层提供，独立核实极难。',
            'invest': '净利润5.61亿，但资本化金额已达14.13亿——是净利润的2.5倍。真实盈利能力存疑。',
            'reg':   '资本化比例长期维持40%以上，且在AI项目商业化不确定的背景下，需评估是否符合谨慎性原则。',
            'cred':  '利润承压，有息负债开始上升。资本化形成的无形资产变现能力接近零，实际偿债资产缩水。',
        },
        'choices': [
            {
                'label': 'A', 'text': '维持约42%资本化率，与往年持平，以稳定财务表现',
                'score': 0,
                'feedback': {
                    'mgmt':  '利润表现稳定，短期压力缓解。但资本化金额持续超过净利润，未来摊销压力积累。这是最符合管理层短期利益的选择。',
                    'acct':  '选择了与往年一致的处理，减少了来自管理层的压力。但星火大模型商业化路径不清晰，资本化依据仍然薄弱，你内心存有疑虑。',
                    'audit': '资本化率未出现异常波动，但绝对金额已是净利润2.5倍。你在底稿中记录了这一风险，但未提出异议，出具标准无保留意见。',
                    'invest': '账面净利润看似稳定，但你发现资本化金额已是净利润2.5倍。调整后公司早已亏损，你开始重新评估持仓。',
                    'reg':   '资本化率未出现异常跳升，暂未触发问询门槛。但长期偏高的资本化比例已进入关注名单。',
                    'cred':  '短期财务指标未恶化，授信维持不变。但无形资产持续膨胀，你已要求在下次评审时重点关注资产质量。',
                },
            },
            {
                'label': 'B', 'text': '主动下调至约30%，体现谨慎性，加强费用化',
                'score': 1,
                'feedback': {
                    'mgmt':  '净利润进一步承压，可能引发投资者对盈利能力的质疑。你面临董事会的压力，这个决定很难持续。',
                    'acct':  '这是最符合谨慎性原则的选择。你坚守了准则，但来自管理层的压力将会更大。职业操守与现实压力的博弈，这只是开始。',
                    'audit': '资本化率下降，审计风险降低。你注意到财务人员主动提高了费用化比例，判断其具有职业审慎性，底稿记录积极。',
                    'invest': '资本化率下调，利润质量明显改善。你对公司财务信息透明度的信心有所提升，这是正向信号。',
                    'reg':   '资本化率下降体现了谨慎性原则，符合监管导向。暂无问询必要，但仍需持续跟踪摊销和减值情况。',
                    'cred':  '费用化比例提升，账面利润有所下降，但盈利质量改善。你调整信用评估模型，给予更高的质量评分。',
                },
            },
            {
                'label': 'C', 'text': '提高至约55%，以最大化当期利润',
                'score': -1,
                'feedback': {
                    'mgmt':  '当期利润大幅改善，各项考核指标达标。但资本化金额已远超净利润，监管问询风险急剧上升，你把一枚定时炸弹埋进了资产端。',
                    'acct':  '你执行了管理层的意图，但内心清楚这已超出了合理判断边界。星火大模型商业化路径不清晰，这些资产的未来价值存在巨大不确定性。',
                    'audit': '资本化率突然大幅上升，触发了重大风险关注。你要求管理层提供每个新增资本化项目的详细技术验证文件，压力骤增。',
                    'invest': '资本化率跳升，你立刻意识到这是利润美化信号。按调整后数据，公司实质已大幅亏损。你开始减仓。',
                    'reg':   '资本化率大幅异常上升，立即触发问询程序。你要求公司逐项目说明资本化依据，并关注是否存在长期挂账风险。',
                    'cred':  '资本化率跳升导致账面资产膨胀，但真实偿债能力下降。你收紧授信条件，要求追加有形资产抵押。',
                },
            },
        ],
    },
    {
        'year': '2023年',
        'title': '深交所问询函到达',
        'desc': '深交所就科大讯飞研发资本化情况发出问询，要求逐项目说明资本化依据、工时分摊方式、开始资本化时点，以及是否存在长期挂账情形。公司需在20个工作日内回复。',
        'stats': [
            {'label': '资本化金额',   'value': '16.02亿', 'delta': '+13.4% YoY'},
            {'label': '净利润',       'value': '6.57亿',  'delta': None},
            {'label': '开发支出余额', 'value': '约10亿+', 'delta': None},
        ],
        'lens': {
            'mgmt':  '问询函是个麻烦，但也是展示合规性的机会。关键是让回复足够充分，打消监管疑虑，同时不暴露判断上的灰色空间。',
            'acct':  '你需要组织内部材料应对问询。部分项目的资本化时点和依据文件并不完整，需要在合规范围内进行整理和补充。',
            'audit': '监管问询的问题和你的审计程序高度重合。你需要重新评估自己的审计证据是否足够，以及无保留意见是否经得起审查。',
            'invest': '监管问询意味着资本化合规性存在疑点。你开始重新审视持仓，等待公司回复内容。',
            'reg':   '问询函已发出。你关注的核心是：公司的回复是否能提供充分、可验证的项目级证据，而非笼统的合规声明。',
            'cred':  '监管关注是信用风险信号。你暂停新增授信审批，等待问询结果。',
        },
        'choices': [
            {
                'label': 'A', 'text': '配合监管，提供完整的逐项目资本化依据和项目进度文件',
                'score': 1,
                'feedback': {
                    'mgmt':  '短期工作量巨大，但透明回复有助于建立监管信任，降低未来被追责的风险。这是正确但痛苦的选择。',
                    'acct':  '你花了大量时间整理项目文件，最终提供了相对完整的回复。职业操守得到坚守，但也暴露了部分项目依据薄弱的问题。',
                    'audit': '公司提供了详尽的项目文件，你重新核查后认为审计证据充分。无保留意见得到支撑，你松了一口气。',
                    'invest': '回复内容详细，信息透明度提升。你恢复了对公司财务信息可信度的部分信心。',
                    'reg':   '回复质量较高，逐项目提供了资本化依据和进度说明。问询风险基本化解，但仍需关注后续摊销和减值情况。',
                    'cred':  '公司配合监管、信息透明，信用风险有所降低。你恢复正常授信审批流程。',
                },
            },
            {
                'label': 'B', 'text': '提供笼统的合规声明，强调"严格遵循会计准则"，避免暴露细节',
                'score': -1,
                'feedback': {
                    'mgmt':  '短期规避了细节披露风险，但监管机构可能发出追问函，要求提供更具体的项目证据，问题只是推迟了。',
                    'acct':  '你执行了管理层的回复策略，但清楚地知道部分项目依据不充分。这份回复让你感到不安——这是一个职业道德的灰色地带。',
                    'audit': '公司回复笼统，你开始重新审视自己的审计底稿。若监管追问深入，你的审计意见可能也会受到质疑。',
                    'invest': '回复内容空洞，没有提供实质性的项目级信息。你的疑虑进一步加深，开始准备离场。',
                    'reg':   '回复质量不达标，决定发出追问函，要求在10个工作日内补充逐项目资本化依据，以及开始资本化的具体时间点和验证文件。',
                    'cred':  '公司应对监管的方式让你担忧信息透明度。你进一步收紧授信，要求月度财务报告。',
                },
            },
            {
                'label': 'C', 'text': '同时启动部分项目资本化率的主动调整，展示监管敏感度',
                'score': 1,
                'feedback': {
                    'mgmt':  '主动调整体现了对监管的响应，有助于建立良好的监管关系。代价是当期利润有所下降，需要向董事会解释。',
                    'acct':  '这是一个平衡合规与现实的选择。主动调整比被动问询更能体现职业判断的诚意，你感到这是相对稳妥的路径。',
                    'audit': '公司主动调整资本化政策，审计风险有所降低。你在底稿中记录了这一政策变化，关注其对财务报表的影响是否已充分披露。',
                    'invest': '公司主动调整资本化率，说明之前的判断存在空间。利润质量有所改善，但信心仍需时间重建。',
                    'reg':   '主动调整体现了对监管导向的积极响应，问询风险基本化解。你记录下这一积极信号，但仍将持续跟踪。',
                    'cred':  '主动调整和配合监管是积极信号，信用评级展望从"负面"调回"稳定"。',
                },
            },
        ],
    },
    {
        'year': '2024年',
        'title': '定增申请：预设40%资本化率',
        'desc': '科大讯飞申请定增募资40亿元，其中教育大模型项目拟投入研发费用5.45亿元，并在申请文件中预先设定40%部分予以资本化。这一预设比例在定增审核问询中引发关注。',
        'stats': [
            {'label': '资本化金额',  'value': '19.96亿', 'delta': '+24.6% YoY'},
            {'label': '净利润',      'value': '5.60亿',  'delta': '-14.8% YoY'},
            {'label': '资产负债率',  'value': '约55%',   'delta': '持续上升'},
        ],
        'lens': {
            'mgmt':  '预设资本化率是为了给投资者提供清晰的财务预期。但监管追问让你意识到，这与准则要求的逐项目判断之间存在明显张力。',
            'acct':  '你在准备定增材料时，对"预设40%资本化率"这一表述提出了内部疑虑，但被管理层以"投资者需要明确预期"为由否决了。',
            'audit': '预设资本化率直接违背了"逐项目、逐阶段动态判断"的准则要求。你需要决定是否在审计报告中提示这一风险。',
            'invest': '公司在项目立项前就预设资本化率，说明资本化决策可能受到财务目标驱动，而非客观项目进展。这是一个重要的质量警示。',
            'reg':   '预设资本化率是本次审核的核心关注点。准则要求根据项目客观进展动态判断，预先锁定比例不符合谨慎性原则，需要公司充分解释。',
            'cred':  '资产负债率已接近55%，定增若成功将缓解财务压力；若失败，偿债风险将进一步上升。预设资本化率暴露了财务规划对会计处理的依赖。',
        },
        'choices': [
            {
                'label': 'A', 'text': '坚持预设比例不变，以"提供投资者明确预期"为理由应对监管追问',
                'score': -1,
                'feedback': {
                    'mgmt':  '监管追问未能化解，定增审核被要求补充材料。你坚持了立场，但代价是审核进程延误，融资计划面临不确定性。',
                    'acct':  '你执行了管理层的决定，但在内部备忘录中记录了自己的疑虑。这是一个你日后可能需要为之辩护的决定。',
                    'audit': '公司坚持预设比例，你决定在审计报告附注中增加关于资本化政策的说明性段落，以提示读者这一判断的特殊性。',
                    'invest': '公司坚持预设比例，监管追问未化解。你认为这是财务目标驱动会计判断的典型信号，决定减持。',
                    'reg':   '坚持预设比例的解释未能令人信服。你要求公司提供每个资本化项目独立的技术可行性验证和商业化路径证明，并暂停审核进度。',
                    'cred':  '审核延误意味着定增融资面临风险，公司短期流动性压力上升。你将授信评级从"稳定"下调至"关注"。',
                },
            },
            {
                'label': 'B', 'text': '调整表述：删除预设比例，改为"根据项目进展逐项判断"，提供项目级依据',
                'score': 1,
                'feedback': {
                    'mgmt':  '主动调整表述显示了对监管的尊重，审核阻力减小。虽然失去了明确的财务预期，但定增推进节奏得以恢复。',
                    'acct':  '这是你坚持内部意见的结果——删除预设比例，回归准则要求。你感到这是本次定增过程中最正确的决定。',
                    'audit': '公司调整表述，回归准则导向。审计风险降低，你不再需要在审计报告中增加额外说明段落。',
                    'invest': '调整表述说明公司对监管导向有足够的敏感度。虽然财务预期有所模糊，但信息质量的改善让你更安心。',
                    'reg':   '调整表述体现了对谨慎性原则的尊重，审核阻力消除。这是一个积极信号，你在监管档案中给予正面记录。',
                    'cred':  '监管阻力化解，定增推进恢复正轨。你恢复正常授信评估，等待定增结果。',
                },
            },
            {
                'label': 'C', 'text': '主动撤回定增申请，重新设计融资方案，彻底规避监管风险',
                'score': 1,
                'feedback': {
                    'mgmt':  '撤回申请是最保守的选择，避免了监管风险，但短期融资缺口需要通过银行借款填补，财务成本上升。你向董事会解释这是为了长期稳健。',
                    'acct':  '撤回申请意味着压力暂时缓解，但公司资金需求依然存在。你开始准备新的融资方案，这次会更注重合规性设计。',
                    'audit': '撤回申请，审计压力解除。但你在内部备忘录中记录：公司对资本化政策的理解需要系统性纠偏，这不是一次性事件。',
                    'invest': '撤回定增是超预期的谨慎信号。公司主动规避了融资风险，虽然短期融资缺口存在，但治理质量的提升让你重新评估长期价值。',
                    'reg':   '主动撤回显示公司对监管意见的高度重视。这一举动显著降低了该公司的监管优先关注级别。',
                    'cred':  '撤回定增意味着短期融资压力上升，但规避了监管风险。你维持授信评级不变，等待新融资方案。',
                },
            },
        ],
    },
]

ENDINGS = {
    'mgmt': {
        'good': ('🏆', '稳健掌舵者', '你在利润压力与合规边界之间找到了相对平衡的路径，避免了最坏的结局。'),
        'mid':  ('⚠️', '灰色地带的博弈者', '部分决策游走在合规边界，短期目标得到了满足，但风险正在积累。'),
        'bad':  ('💣', '定时炸弹的埋设者', '激进的资本化策略在短期内维持了报表美观，但减值风险和监管压力已经逼近临界点。'),
    },
    'acct': {
        'good': ('⚖️', '职业底线的守护者', '在巨大压力下坚守了准则要求，你的职业操守经受住了考验。'),
        'mid':  ('🌊', '被激流推着走的执行者', '你执行了指令，内心保留了疑虑，但行动上让步了。这是大多数人在真实压力下的真实写照。'),
        'bad':  ('🚨', '职业操守的失守者', '准则被当成了工具，职业判断沦为了利润调节的外衣。这是这个角色最危险的结局。'),
    },
    'audit': {
        'good': ('🔎', '独立意见的捍卫者', '你在信息不对称的困境中，尽可能地核实了证据，维护了审计独立性。'),
        'mid':  ('📋', '底稿记录者', '你发现了问题，但选择了记录而非行动。独立意见的边界，你走在了中间地带。'),
        'bad':  ('❌', '背书者', '审计压力下，你接受了管理层的判断。无保留意见背后，是对外部信息使用者的责任缺失。'),
    },
    'invest': {
        'good': ('📊', '穿透分析的理性者', '你没有被账面利润迷惑，通过数据穿透发现了真实的盈利质量问题，保护了自己的投资利益。'),
        'mid':  ('🎲', '信息博弈的参与者', '你意识到了风险，但行动有些迟缓。部分损失源于信息不对称，部分源于判断的犹豫。'),
        'bad':  ('💸', '信息不对称的受害者', '你依赖了经过资本化美化的财务数据，在盈利质量陷阱中做出了错误判断。'),
    },
    'reg': {
        'good': ('⚖️', '市场秩序的守护者', '你的问询和审查有效地推动了信息披露质量的提升，维护了会计准则的权威。'),
        'mid':  ('📁', '文件归档者', '你记录了风险，但未能在关键节点采取更强硬的行动。监管效果打了折扣。'),
        'bad':  ('🕳️', '监管盲区的制造者', '问询流于形式，未能穿透管理层的自我声明。市场信息质量在你的监管区间内持续恶化。'),
    },
    'cred': {
        'good': ('🏦', '风险穿透的银行家', '你识别了无形资产的虚高风险，及时调整了授信策略，保护了债权人利益。'),
        'mid':  ('📉', '被动应对者', '你在风险信号出现后有所反应，但没有及时建立更完善的穿透分析机制。'),
        'bad':  ('🔥', '隐性杠杆的承担者', '你被美化的资产结构蒙蔽，实际授信风险远高于账面显示。一旦无形资产减值，你将是最大的受害者。'),
    },
}

VERDICT_TEXT = {
    'good': '你的判断总体审慎，体现了对准则精神的尊重和对风险的清醒认识。在真实案例中，这类决策往往能够抵御监管审查和时间的检验。',
    'mid':  '你在审慎与现实之间摇摆，部分决策让步于短期压力。这是多数从业者在真实压力下的真实写照——准则的理想与商业的现实之间，永远存在张力。',
    'bad':  '你的判断过于倾向短期利益，忽视了风险的累积效应。在真实的科大讯飞案例中，这类决策最终引发了深交所的问询和外部的广泛质疑。',
}

st.markdown("""
<style>
[data-testid="stAppViewContainer"] { max-width: 720px; margin: auto; }
.scene-box { background:#f8f9fa; border-radius:12px; padding:1.2rem 1.4rem; margin-bottom:1rem; }
.lens-box { border-left:4px solid #1a73e8; background:#e8f0fe; padding:.75rem 1rem;
            border-radius:0 8px 8px 0; margin-bottom:1rem; font-size:.93rem; }
.feedback-box { background:#f0f4ff; border-radius:10px; padding:1rem 1.2rem; margin-top:.75rem;
                border-left:4px solid #4285f4; font-size:.93rem; }
.verdict-box { background:#f8f9fa; border-radius:12px; padding:1rem 1.2rem;
               text-align:left; margin:1rem 0; }
</style>
""", unsafe_allow_html=True)

# ── Session state ──

def init():
    defaults = {'phase': 'intro', 'role': None, 'scene_idx': 0,
                'scores': [], 'chosen': None, 'show_feedback': False}
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init()

def role_info(rid):
    return next(r for r in ROLES if r['id'] == rid)

def get_category(scores):
    t = sum(scores)
    return 'good' if t >= 2 else ('mid' if t >= 0 else 'bad')

def restart():
    for k in ['phase','role','scene_idx','scores','chosen','show_feedback']:
        del st.session_state[k]
    init()

# ── INTRO ──

if st.session_state.phase == 'intro':
    st.markdown('## 🏢 财务判断室')
    st.markdown('**科大讯飞研发资本化争议 · 角色扮演**')
    st.markdown('选择你的身份，经历三个真实事件节点，做出你的判断。')
    st.markdown('---')
    st.markdown('#### 选择角色')

    cols = st.columns(3)
    for i, r in enumerate(ROLES):
        with cols[i % 3]:
            selected = st.session_state.role == r['id']
            if st.button(
                f"{r['icon']} **{r['name']}**\n\n{r['desc']}",
                key=f"role_{r['id']}",
                use_container_width=True,
                type='primary' if selected else 'secondary'
            ):
                st.session_state.role = r['id']
                st.rerun()

    st.markdown('---')
    if st.session_state.role:
        ri = role_info(st.session_state.role)
        st.info(f"已选择：{ri['icon']} **{ri['name']}** — {ri['desc']}")
        if st.button('开始游戏 →', type='primary', use_container_width=True):
            st.session_state.phase = 'scene'
            st.session_state.scene_idx = 0
            st.session_state.scores = []
            st.session_state.chosen = None
            st.session_state.show_feedback = False
            st.rerun()
    else:
        st.button('请先选择角色', disabled=True, use_container_width=True)

# ── SCENE ──

elif st.session_state.phase == 'scene':
    idx = st.session_state.scene_idx
    scene = SCENES[idx]
    role = st.session_state.role
    ri = role_info(role)

    pct = int((idx / len(SCENES)) * 100)
    st.progress(pct, text=f'场景 {idx+1} / {len(SCENES)}')

    st.markdown(f"### {scene['year']} · {scene['title']}")
    st.markdown(f"<div class='scene-box'>{scene['desc']}</div>", unsafe_allow_html=True)

    cols = st.columns(3)
    for i, stat in enumerate(scene['stats']):
        with cols[i]:
            st.metric(stat['label'], stat['value'], stat['delta'])

    st.markdown(
        f"<div class='lens-box'><strong>{ri['icon']} {ri['name']}视角：</strong>"
        f"{scene['lens'][role]}</div>",
        unsafe_allow_html=True
    )

    st.markdown('**你的决策：**')
    already_chosen = st.session_state.show_feedback
    chosen_idx = st.session_state.chosen

    for i, c in enumerate(scene['choices']):
        btn_label = f"**{c['label']}.** {c['text']}"
        if already_chosen:
            st.button(btn_label, key=f'ch_{idx}_{i}',
                      disabled=(i != chosen_idx),
                      type='primary' if i == chosen_idx else 'secondary',
                      use_container_width=True)
        else:
            if st.button(btn_label, key=f'ch_{idx}_{i}',
                         use_container_width=True, type='secondary'):
                st.session_state.chosen = i
                st.session_state.show_feedback = True
                st.session_state.scores.append(c['score'])
                st.rerun()

    if st.session_state.show_feedback and chosen_idx is not None:
        fb = scene['choices'][chosen_idx]['feedback'][role]
        st.markdown(
            f"<div class='feedback-box'><strong>选择结果：</strong><br>{fb}</div>",
            unsafe_allow_html=True
        )
        st.markdown('')
        is_last = (idx == len(SCENES) - 1)
        if st.button('查看最终结局 →' if is_last else '下一个场景 →',
                     type='primary', use_container_width=True):
            if is_last:
                st.session_state.phase = 'ending'
            else:
                st.session_state.scene_idx += 1
                st.session_state.chosen = None
                st.session_state.show_feedback = False
            st.rerun()

# ── ENDING ──

elif st.session_state.phase == 'ending':
    role = st.session_state.role
    ri = role_info(role)
    cat = get_category(st.session_state.scores)
    icon, title, sub = ENDINGS[role][cat]

    st.markdown('---')
    st.markdown(f"<div style='text-align:center;font-size:3rem'>{icon}</div>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center'>{title}</h2>", unsafe_allow_html=True)
    st.markdown(
        f"<p style='text-align:center;color:#555'>{ri['icon']} <strong>{ri['name']}</strong>的结局<br>{sub}</p>",
        unsafe_allow_html=True
    )

    dot_html = ''.join(
        f"<span style='display:inline-block;width:14px;height:14px;border-radius:50%;"
        f"background:{'#3d8b37' if s > 0 else '#c62828' if s < 0 else '#e65100'};"
        f"margin:0 4px'></span>"
        for s in st.session_state.scores
    )
    st.markdown(
        f"<div style='text-align:center;margin:1rem 0'>{dot_html}</div>"
        f"<p style='text-align:center;font-size:.8rem;color:#888'>绿色=审慎 · 红色=激进 · 橙色=中性</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='verdict-box'>"
        f"<p style='font-size:.8rem;font-weight:600;color:#888;margin-bottom:.5rem;"
        f"text-transform:uppercase;letter-spacing:.05em'>案例对照分析</p>"
        f"<p>{VERDICT_TEXT[cat]}</p></div>",
        unsafe_allow_html=True
    )

    tag_map = {
        'good': [('✅ 合规导向','#e8f5e9','#2e7d32'), ('✅ 职业审慎','#e3f2fd','#1565c0'), ('✅ 风险识别','#e3f2fd','#1565c0')],
        'mid':  [('⚠️ 压力妥协','#fff8e1','#e65100'), ('⚠️ 信息不对称','#e3f2fd','#1565c0'), ('⚠️ 灰色地带','#fff8e1','#e65100')],
        'bad':  [('❌ 激进处理','#ffebee','#c62828'), ('❌ 利润驱动','#ffebee','#c62828'), ('⚠️ 监管风险','#fff8e1','#e65100')],
    }
    tags_html = ''.join(
        f"<span style='display:inline-block;background:{bg};color:{fg};"
        f"padding:4px 10px;border-radius:6px;font-size:.8rem;margin:2px'>{t}</span>"
        for t, bg, fg in tag_map[cat]
    )
    st.markdown(f"<div style='margin:.5rem 0'>{tags_html}</div>", unsafe_allow_html=True)

    st.markdown('---')
    c1, c2 = st.columns(2)
    with c1:
        if st.button('🔄 换个角色再玩', use_container_width=True):
            restart()
            st.rerun()
    with c2:
        if st.button('📖 查看完整报告分析', use_container_width=True, type='primary'):
            st.info('可将完整报告链接或PDF放在这里共享给玩家。')
