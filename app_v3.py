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
        'desc': '科大讯飞全年研发投入33.55亿元，利润承压（净利润仅5.61亿）。星火大模型正式立项，技术可行性已初步验证，但商业化路径尚不明朗。',
        'stats': [
            {'label': '研发总投入', 'value': '33.55亿', 'delta': None},
            {'label': '净利润',     'value': '5.61亿',  'delta': '-63.9% YoY'},
            {'label': '上年资本化率','value': '42.10%', 'delta': None},
        ],
        'lens': {
            'mgmt':   '利润已大幅下滑，若再压低资本化比例，净利润将跌破5亿，影响高管薪酬考核和定增资质。',
            'acct':   '准则要求逐项目判断，但管理层已明示"不能让利润太难看"。星火大模型商业化路径不清晰，资本化依据存疑。',
            'audit':  '需核查星火大模型是否满足五项资本化条件，但技术验证文件由管理层提供，独立核实极难。',
            'invest': '净利润5.61亿，但资本化金额已达14.13亿——是净利润的2.5倍。真实盈利能力存疑。',
            'reg':    '资本化比例长期维持40%以上，且在AI项目商业化不确定的背景下，需评估是否符合谨慎性原则。',
            'cred':   '利润承压，有息负债开始上升。资本化形成的无形资产变现能力接近零，实际偿债资产缩水。',
        },
        'role_choices': {
            'mgmt': [
                {'label': 'A', 'text': '维持约42%资本化率，与往年持平，稳定财务表现',
                 'score': 0,
                 'feedback': '利润表现稳定，短期压力缓解。但资本化金额持续超过净利润，未来摊销压力积累。这是最符合管理层短期利益的选择，但风险在悄悄滋生。'},
                {'label': 'B', 'text': '主动下调至约30%，体现谨慎性，主动加强费用化',
                 'score': 1,
                 'feedback': '净利润进一步承压，可能引发投资者对盈利能力的质疑。你面临董事会的压力，但这一决定更能体现长期稳健的经营理念。'},
                {'label': 'C', 'text': '提高至约55%，以最大化当期利润，达成考核目标',
                 'score': -1,
                 'feedback': '当期利润大幅改善，各项考核指标达标。但资本化金额已远超净利润，监管问询风险急剧上升，你把一枚定时炸弹埋进了资产端。'},
            ],
            'acct': [
                {'label': 'A', 'text': '按管理层指示维持42%，以"与往年一致"作为账务依据',
                 'score': 0,
                 'feedback': '选择了与往年一致的处理，减少了来自管理层的压力。但星火大模型商业化路径不清晰，资本化依据仍然薄弱，你内心存有疑虑。'},
                {'label': 'B', 'text': '坚持逐项目评估，据实下调至30%并向管理层书面说明',
                 'score': 1,
                 'feedback': '这是最符合谨慎性原则的选择。你坚守了准则，但来自管理层的压力将会更大。职业操守与现实压力的博弈，这只是开始。'},
                {'label': 'C', 'text': '执行管理层要求的55%，在备忘录中保留书面异议记录',
                 'score': -1,
                 'feedback': '你执行了管理层的意图，虽留有书面记录，但内心清楚这已超出了合理判断边界。星火大模型商业化路径不清晰，这些资产的未来价值存在巨大不确定性。'},
            ],
            'audit': [
                {'label': 'A', 'text': '要求管理层提供每个资本化项目的独立技术可行性证明及工时分摊记录',
                 'score': 1,
                 'feedback': '你严格执行了审计程序。管理层提供了文件，但部分内容难以独立核实。你在底稿中如实记录了信息不对称风险，审计独立性得到维护。'},
                {'label': 'B', 'text': '查阅管理层提供的项目立项文件，认为整体合理，出具无保留意见',
                 'score': 0,
                 'feedback': '资本化率未出现异常波动，但绝对金额已是净利润2.5倍。你在底稿中记录了这一风险，但未进一步追查，出具标准无保留意见。'},
                {'label': 'C', 'text': '接受管理层对资本化率的合理性声明，不做深度核查，优先完成审计',
                 'score': -1,
                 'feedback': '审计压力下，你接受了管理层的判断。无保留意见背后，是对外部信息使用者的责任缺失。若后续监管问询，你的审计底稿将面临严苛审查。'},
            ],
            'invest': [
                {'label': 'A', 'text': '深度分析：剔除资本化影响，还原真实盈利能力后再做判断',
                 'score': 1,
                 'feedback': '你没有被账面利润迷惑，调整后发现公司实质已接近亏损。资本化金额是净利润的2.5倍——这是重要的质量警示，你决定谨慎持有并持续跟踪。'},
                {'label': 'B', 'text': '关注净利润指标，认为5.61亿利润尚可接受，维持现有持仓',
                 'score': 0,
                 'feedback': '账面净利润看似稳定，但你忽视了资本化的放大效应。风险正在悄悄积累，你的持仓面临潜在的估值重估压力。'},
                {'label': 'C', 'text': '看好AI大模型前景，忽略资本化问题，追加投资扩大持仓',
                 'score': -1,
                 'feedback': '你被AI叙事驱动，忽视了财务信号。资本化金额已是净利润2.5倍，真实盈利能力存疑。在信息不对称下追加投资，你承担了超出预期的风险。'},
            ],
            'reg': [
                {'label': 'A', 'text': '启动专项核查：要求公司逐项目说明资本化依据，评估是否符合谨慎性原则',
                 'score': 1,
                 'feedback': '你的主动核查有效推动了信息披露质量。公司提供的解释揭示了部分项目依据薄弱，监管介入时机恰当，有效维护了市场信息质量。'},
                {'label': 'B', 'text': '将该公司列入重点关注名单，持续跟踪，暂不主动问询',
                 'score': 0,
                 'feedback': '资本化率未出现异常跳升，暂未触发问询门槛。但长期偏高的资本化比例已进入关注名单，你记录了这一风险，等待进一步信号。'},
                {'label': 'C', 'text': '认为公司已按准则披露，无需额外关注，常规审查即可',
                 'score': -1,
                 'feedback': '未能识别资本化长期偏高的风险信号。监管效果打了折扣，市场信息质量在你的监管区间内持续积累风险，为后续问询埋下隐患。'},
            ],
            'cred': [
                {'label': 'A', 'text': '穿透分析：剔除无形资产后重新评估偿债能力，据此调整授信额度',
                 'score': 1,
                 'feedback': '你识别了无形资产的虚高风险，及时调整了授信策略。剔除开发支出后，真实资产质量大幅缩水，你已要求追加有形资产抵押，保护了债权人利益。'},
                {'label': 'B', 'text': '关注利润与负债指标，短期指标未恶化，维持现有授信不变',
                 'score': 0,
                 'feedback': '短期财务指标未恶化，授信维持不变。但无形资产持续膨胀，你已要求在下次评审时重点关注资产质量，风险正在积累。'},
                {'label': 'C', 'text': '基于账面资产总额评估，认为偿债能力充足，主动扩大授信',
                 'score': -1,
                 'feedback': '你被账面资产总量迷惑，忽视了无形资产变现能力接近零的事实。实际偿债资产严重缩水，一旦发生减值，你将是最大的受害者。'},
            ],
        },
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
            'mgmt':   '问询函是个麻烦，但也是展示合规性的机会。关键是让回复足够充分，打消监管疑虑，同时不暴露判断上的灰色空间。',
            'acct':   '你需要组织内部材料应对问询。部分项目的资本化时点和依据文件并不完整，需要在合规范围内进行整理和补充。',
            'audit':  '监管问询的问题和你的审计程序高度重合。你需要重新评估自己的审计证据是否足够，以及无保留意见是否经得起审查。',
            'invest': '监管问询意味着资本化合规性存在疑点。你开始重新审视持仓，等待公司回复内容。',
            'reg':    '问询函已发出。你关注的核心是：公司的回复是否能提供充分、可验证的项目级证据，而非笼统的合规声明。',
            'cred':   '监管关注是信用风险信号。你暂停新增授信审批，等待问询结果。',
        },
        'role_choices': {
            'mgmt': [
                {'label': 'A', 'text': '全力配合：组织团队提供完整的逐项目资本化依据和项目进度文件',
                 'score': 1,
                 'feedback': '短期工作量巨大，但透明回复有助于建立监管信任，降低未来被追责的风险。这是正确但痛苦的选择。'},
                {'label': 'B', 'text': '最小披露：提供笼统合规声明，强调"严格遵循准则"，避免暴露细节',
                 'score': -1,
                 'feedback': '短期规避了细节披露风险，但监管机构可能发出追问函，要求提供更具体的项目证据，问题只是推迟了。'},
                {'label': 'C', 'text': '主动调整：同时宣布下调资本化率，以行动回应监管关切',
                 'score': 1,
                 'feedback': '主动调整体现了对监管的响应，有助于建立良好的监管关系。代价是当期利润有所下降，需要向董事会解释，但长期风险显著降低。'},
            ],
            'acct': [
                {'label': 'A', 'text': '据实整理所有项目文件，不足之处如实说明，由管理层决定是否披露',
                 'score': 1,
                 'feedback': '你花了大量时间整理项目文件，最终提供了相对完整的回复。职业操守得到坚守，也暴露了部分项目依据薄弱的问题，但你保住了底线。'},
                {'label': 'B', 'text': '补充完善文件逻辑，在合规边界内"优化"材料表述以符合资本化条件',
                 'score': -1,
                 'feedback': '你在合规与"包装"之间走钢丝。部分材料的事后完善已接近职业道德的灰色地带，若监管进一步核查原始记录，风险将暴露。'},
                {'label': 'C', 'text': '向管理层书面提示材料不足的问题，并建议主动下调资本化率',
                 'score': 1,
                 'feedback': '这是最体现职业判断的选择。你不仅如实整理了材料，还主动提出了改进建议。这份建议可能让你承压，但也是你最有力的职业保护。'},
            ],
            'audit': [
                {'label': 'A', 'text': '主动重新核查审计底稿，评估无保留意见是否仍然成立',
                 'score': 1,
                 'feedback': '公司提供了详尽的项目文件，你重新核查后认为审计证据充分。无保留意见得到支撑，审计独立性经受住了监管压力的检验。'},
                {'label': 'B', 'text': '等待公司回复结果，再判断是否需要补充审计程序',
                 'score': 0,
                 'feedback': '被动等待的策略让你暂时避免了额外工作，但若公司回复笼统，你的审计底稿将面临更大的质疑压力，主动性的缺失是一个隐患。'},
                {'label': 'C', 'text': '认为已出具无保留意见，监管问询是公司的问题，无需主动介入',
                 'score': -1,
                 'feedback': '监管问询的核心关切与你的审计范围高度重合，置身事外的态度难以为继。若后续追责，"已出具无保留意见"并不能成为免责的盾牌。'},
            ],
            'invest': [
                {'label': 'A', 'text': '等待并深度解读公司回复，根据信息质量决定是否减持',
                 'score': 1,
                 'feedback': '回复内容详细，信息透明度提升，你恢复了对公司财务信息可信度的部分信心。这种以信息质量为核心的判断逻辑是价值投资的体现。'},
                {'label': 'B', 'text': '监管问询属于常规事项，不影响AI大模型的长期逻辑，维持持仓',
                 'score': 0,
                 'feedback': '你以长期逻辑覆盖了短期风险信号。若公司回复透明，这一判断尚可接受；若回复笼统，你将面临更大的信息风险。'},
                {'label': 'C', 'text': '监管问询是重大风险信号，立即减持规避不确定性',
                 'score': 0,
                 'feedback': '你对监管信号的反应及时，避免了后续可能的更大损失。但过早离场也让你错失了公司若能充分回复后的修复机会，判断的时机是投资的核心技能。'},
            ],
            'reg': [
                {'label': 'A', 'text': '逐项审核回复内容，要求对薄弱项目补充可验证的原始证据',
                 'score': 1,
                 'feedback': '回复质量较高，逐项目提供了资本化依据和进度说明。你的严格审核有效提升了信息披露质量，问询风险基本化解，监管目标达成。'},
                {'label': 'B', 'text': '回复声称合规即可结案，不做深入核查，避免过度干预市场',
                 'score': -1,
                 'feedback': '回复质量不达标，但未能识别。笼统的合规声明通过了审查，监管效果流于形式，市场信息质量并未得到真正改善。'},
                {'label': 'C', 'text': '回复不充分，发出追问函，要求10个工作日内补充逐项目资本化依据',
                 'score': 1,
                 'feedback': '你对回复质量的判断准确，追问函的发出给公司施加了实质性压力。这正是监管应有的力度，有效推动了信息透明度提升。'},
            ],
            'cred': [
                {'label': 'A', 'text': '暂停新增授信，等待问询结果，同时启动授信条件重审',
                 'score': 1,
                 'feedback': '公司配合监管、信息透明，信用风险有所降低。暂停授信的谨慎态度保护了你的风险敞口，重审结果将为后续授信提供更可靠的依据。'},
                {'label': 'B', 'text': '监管问询属于披露事项，不影响偿债能力，维持授信不变',
                 'score': 0,
                 'feedback': '短期判断尚可接受，但监管问询暗示的资产质量风险尚未消化。若后续减值发生，你的授信风险将被动放大。'},
                {'label': 'C', 'text': '收紧授信条件，要求追加有形资产抵押并提供月度财务报告',
                 'score': 1,
                 'feedback': '你对监管信号的反应迅速且有据可依，收紧授信条件有效降低了风险敞口。公司应对监管的方式将是下一步评估授信的核心依据。'},
            ],
        },
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
            'mgmt':   '预设资本化率是为了给投资者提供清晰的财务预期。但监管追问让你意识到，这与准则要求的逐项目判断之间存在明显张力。',
            'acct':   '你在准备定增材料时，对"预设40%资本化率"这一表述提出了内部疑虑，但被管理层以"投资者需要明确预期"为由否决了。',
            'audit':  '预设资本化率直接违背了"逐项目、逐阶段动态判断"的准则要求。你需要决定是否在审计报告中提示这一风险。',
            'invest': '公司在项目立项前就预设资本化率，说明资本化决策可能受到财务目标驱动，而非客观项目进展。这是一个重要的质量警示。',
            'reg':    '预设资本化率是本次审核的核心关注点。准则要求根据项目客观进展动态判断，预先锁定比例不符合谨慎性原则，需要公司充分解释。',
            'cred':   '资产负债率已接近55%，定增若成功将缓解财务压力；若失败，偿债风险将进一步上升。预设资本化率暴露了财务规划对会计处理的依赖。',
        },
        'role_choices': {
            'mgmt': [
                {'label': 'A', 'text': '调整表述：删除预设比例，改为"根据项目进展逐项判断"并提供项目级依据',
                 'score': 1,
                 'feedback': '主动调整表述显示了对监管的尊重，审核阻力减小。虽然失去了明确的财务预期，但定增推进节奏得以恢复，长期信用得到维护。'},
                {'label': 'B', 'text': '坚持预设比例，以"向投资者提供明确财务预期"为由应对监管追问',
                 'score': -1,
                 'feedback': '监管追问未能化解，定增审核被要求补充材料。你坚持了立场，但代价是审核进程延误，融资计划面临不确定性，且监管信任度下降。'},
                {'label': 'C', 'text': '主动撤回定增申请，重新设计合规的融资方案',
                 'score': 1,
                 'feedback': '撤回申请是最保守的选择，避免了监管风险，但短期融资缺口需要通过银行借款填补，财务成本上升。你向董事会解释这是为了长期稳健。'},
            ],
            'acct': [
                {'label': 'A', 'text': '向管理层书面说明预设比例违反准则，建议修改为动态判断表述',
                 'score': 1,
                 'feedback': '这是你坚持内部意见的结果——回归准则要求。你感到这是本次定增过程中最正确的决定，也为自己保留了最有力的职业保护。'},
                {'label': 'B', 'text': '按管理层要求准备材料，在内部备忘录中记录自己的保留意见',
                 'score': 0,
                 'feedback': '你执行了管理层的决定，但在内部备忘录中记录了自己的疑虑。这是一个你日后可能需要为之辩护的决定，备忘录是唯一的保护。'},
                {'label': 'C', 'text': '协助管理层将预设比例包装为"历史资本化率的延续"，以增强说服力',
                 'score': -1,
                 'feedback': '你帮助构建了一个可能误导监管的表述框架。若定增被否或后续监管追查，你的职业责任将难以回避，这是职业操守的严重失守。'},
            ],
            'audit': [
                {'label': 'A', 'text': '在审计报告中增加强调事项段，说明预设资本化率与准则要求的差异',
                 'score': 1,
                 'feedback': '公司坚持预设比例，你在审计报告附注中增加了说明性段落，有效提示了读者这一判断的特殊性。审计独立性得到维护，信息使用者受到保护。'},
                {'label': 'B', 'text': '与管理层沟通要求修改表述，若拒绝则考虑出具保留意见',
                 'score': 1,
                 'feedback': '你对预设比例的合规性问题采取了实质性立场，审计压力传递有效。管理层若修改，审计风险降低；若坚持，保留意见将是信息市场的重要信号。'},
                {'label': 'C', 'text': '认为预设比例属于管理层判断范围，不影响整体审计意见',
                 'score': -1,
                 'feedback': '预设资本化率直接违背了准则的逐项目判断要求，将其归入"管理层判断"是对审计责任的回避。若后续出现问题，无保留意见将难以为继。'},
            ],
            'invest': [
                {'label': 'A', 'text': '将预设资本化率视为财务目标驱动会计的信号，重新评估估值并准备减持',
                 'score': 1,
                 'feedback': '预设资本化率说明资本化决策受财务目标驱动，而非客观进展。你的判断准确，按调整后数据，公司已实质大幅亏损，减持决策有充分依据。'},
                {'label': 'B', 'text': '等待定增结果，若成功则认为监管已背书，继续持有',
                 'score': -1,
                 'feedback': '将监管审核通过等同于财务质量背书是危险的误判。定增成功只意味着融资合规，并不代表资本化处理没有问题，你的持仓风险并未消除。'},
                {'label': 'C', 'text': '关注定增募集资金用途，认为新资金将改善基本面，趁机加仓',
                 'score': -1,
                 'feedback': '在资本化质量存疑的情况下追加投资，你放大了信息不对称风险。预设比例暴露的财务目标驱动问题，是系统性风险的信号，而非加仓机会。'},
            ],
            'reg': [
                {'label': 'A', 'text': '要求公司逐项目提供独立的技术可行性验证，不接受预设比例解释，暂停审核',
                 'score': 1,
                 'feedback': '坚持预设比例的解释未能令人信服，你暂停审核并要求补充独立验证。这是监管应有的力度，有效防止了不合规的融资方案通过，维护了市场秩序。'},
                {'label': 'B', 'text': '要求公司修改表述为"动态判断"，将实质合规性留给公司自行保证',
                 'score': 0,
                 'feedback': '调整表述的要求化解了表面风险，但若公司只改措辞不改实质，监管效果将流于形式。你记录了这一风险，但监管深度仍有提升空间。'},
                {'label': 'C', 'text': '认为40%符合历史惯例，不构成重大合规问题，批准定增申请',
                 'score': -1,
                 'feedback': '以"历史惯例"为由忽视预设比例的合规问题，是对准则精神的误解。这一监管盲区将为后续更大的风险积累提供空间，市场信息质量在此受损。'},
            ],
            'cred': [
                {'label': 'A', 'text': '分析两种情景：定增成功vs失败，分别评估偿债风险并制定应对预案',
                 'score': 1,
                 'feedback': '情景分析帮助你提前做好了风险准备。定增成功则缓解压力，失败则启动预案。这种前瞻性的信用管理有效保护了债权人利益。'},
                {'label': 'B', 'text': '认为定增成功概率高，基于融资后的改善预期扩大授信',
                 'score': -1,
                 'feedback': '基于尚未确定的定增结果扩大授信，你放大了信用风险。预设资本化率暴露的财务规划对会计处理的依赖，是更深层的治理问题，不应被融资预期掩盖。'},
                {'label': 'C', 'text': '资产负债率已达55%，收紧授信并要求将定增募集资金部分用于偿债',
                 'score': 1,
                 'feedback': '你准确识别了55%资产负债率的风险临界点，收紧授信并设定条件是合理的债权人保护措施。这一要求可能影响与公司的关系，但保护了你的实质利益。'},
            ],
        },
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

# ─────────────────────────────────────────────
# 动态样式 — 卡片式布局 + 动画效果
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700;900&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', sans-serif !important;
}

/* ===== 全局背景：淡灰蓝渐变 ===== */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf3 50%, #eef1f6 100%) !important;
    max-width: 760px;
    margin: auto;
}
[data-testid="stMain"] {
    background: transparent !important;
    padding: 1rem 1.5rem !important;
}
[data-testid="stHeader"] {
    background: transparent !important;
}
body, .stApp {
    background: transparent !important;
    color: #1a2332 !important;
}

/* ===== 入场动画 ===== */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}
@keyframes slideInRight {
    from { opacity: 0; transform: translateX(30px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.03); }
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
}
@keyframes shimmer {
    0%   { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

/* ===== 主卡片容器 ===== */
.main-card {
    background: #ffffff;
    border-radius: 24px;
    padding: 2.2rem 2rem;
    margin: 1.2rem auto;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06), 0 1px 4px rgba(0, 0, 0, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.8);
    animation: fadeInUp 0.6s ease-out both;
}

/* ===== 标题区 ===== */
.hero-title {
    text-align: center;
    font-size: 2.1rem;
    font-weight: 900;
    color: #1e3a5f;
    letter-spacing: -0.02em;
    margin-bottom: 0.3rem;
}
.hero-subtitle {
    text-align: center;
    font-size: 0.95rem;
    color: #7a8aa5;
    font-weight: 500;
    margin-bottom: 1.5rem;
}

/* ===== 信息卡片（带图标标题） ===== */
.info-card {
    background: linear-gradient(135deg, #f8fafd 0%, #f0f4f9 100%);
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 1.2rem 1.4rem;
    margin: 0.8rem 0;
    animation: fadeInUp 0.5s ease-out both;
    transition: all 0.25s ease;
}
.info-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);
    border-color: #c8d4e5;
}
.info-card-icon {
    font-size: 1.4rem;
    margin-right: 0.5rem;
    vertical-align: middle;
}
.info-card-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #1e3a5f;
    margin-bottom: 0.4rem;
}
.info-card-body {
    font-size: 0.9rem;
    color: #4a5a72;
    line-height: 1.7;
    font-weight: 400;
}

/* ===== 场景盒子 ===== */
.scene-box {
    background: linear-gradient(135deg, #fafbfc 0%, #f5f7fa 100%);
    border: 1.5px solid #e2e8f0;
    border-radius: 20px;
    padding: 1.4rem 1.6rem;
    margin: 1rem 0 1.2rem;
    color: #2a3441;
    font-size: 0.95rem;
    line-height: 1.85;
    animation: fadeInUp 0.6s ease-out both;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
    font-weight: 400;
}

/* ===== 视角盒子 ===== */
.lens-box {
    background: linear-gradient(135deg, #eef4ff 0%, #e6eeff 100%);
    border: 1.5px solid #c8d8f8;
    border-left: 5px solid #3b6fd8;
    border-radius: 0 18px 18px 0;
    padding: 1.1rem 1.4rem;
    margin: 1rem 0 1.2rem;
    font-size: 0.92rem;
    line-height: 1.75;
    color: #1a2e60;
    animation: slideInRight 0.5s ease-out both;
    box-shadow: 0 2px 10px rgba(60, 100, 200, 0.06);
}
.lens-box strong {
    color: #2255bb;
    font-weight: 700;
}

/* ===== 反馈盒子 ===== */
.feedback-box {
    background: linear-gradient(135deg, #edf8f2 0%, #e4f4eb 100%);
    border: 1.5px solid #b8e4ce;
    border-left: 5px solid #1e8e52;
    border-radius: 0 18px 18px 0;
    padding: 1.1rem 1.4rem;
    margin-top: 0.9rem;
    font-size: 0.92rem;
    line-height: 1.75;
    color: #0d3b22;
    animation: fadeInUp 0.5s ease-out both;
    box-shadow: 0 2px 10px rgba(0, 100, 50, 0.05);
}
.feedback-box strong {
    color: #1e8e52;
    font-weight: 700;
}

/* ===== 决策卡片 ===== */
.choice-card {
    background: #ffffff;
    border: 1.8px solid #d0d8e8;
    border-radius: 16px;
    padding: 1.2rem 1.3rem;
    margin: 0.5rem 0;
    transition: all 0.25s ease;
    cursor: pointer;
    animation: fadeInUp 0.4s ease-out both;
}
.choice-card:hover {
    border-color: #3b6fd8;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(60, 100, 200, 0.12);
}
.choice-card .choice-label {
    display: inline-block;
    background: linear-gradient(135deg, #3b6fd8, #2563eb);
    color: white;
    font-weight: 700;
    width: 32px;
    height: 32px;
    line-height: 32px;
    text-align: center;
    border-radius: 50%;
    margin-right: 0.8rem;
    font-size: 0.9rem;
    vertical-align: top;
}
.choice-card .choice-text {
    display: inline-block;
    font-size: 0.92rem;
    color: #1a2332;
    line-height: 1.6;
    font-weight: 500;
}

/* ===== 角色选择卡片 ===== */
.role-card {
    background: #ffffff;
    border: 2px solid #d8e0ec;
    border-radius: 20px;
    padding: 1.4rem 1rem;
    text-align: center;
    transition: all 0.3s ease;
    cursor: pointer;
    animation: fadeInUp 0.4s ease-out both;
}
.role-card:hover {
    border-color: #3b6fd8;
    transform: translateY(-4px);
    box-shadow: 0 10px 28px rgba(60, 100, 200, 0.15);
}
.role-card.selected {
    border-color: #2563eb;
    background: linear-gradient(135deg, #eef4ff, #e6eeff);
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.15);
    animation: pulse 0.4s ease;
}
.role-card .role-icon {
    font-size: 2.4rem;
    margin-bottom: 0.5rem;
    animation: float 3s ease-in-out infinite;
}
.role-card .role-name {
    font-size: 1.1rem;
    font-weight: 700;
    color: #1e3a5f;
    margin-bottom: 0.3rem;
}
.role-card .role-desc {
    font-size: 0.8rem;
    color: #7a8aa5;
    line-height: 1.5;
    font-weight: 400;
}

/* ===== 结局卡片 ===== */
.ending-card {
    background: #ffffff;
    border-radius: 24px;
    padding: 2.5rem 2rem;
    margin: 1.5rem 0;
    text-align: center;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
    animation: fadeInUp 0.7s ease-out both;
}
.ending-icon {
    font-size: 4rem;
    margin-bottom: 1rem;
    animation: float 3s ease-in-out infinite;
}
.ending-title {
    font-size: 1.8rem;
    font-weight: 900;
    margin-bottom: 0.4rem;
    letter-spacing: -0.01em;
}
.ending-role {
    font-size: 0.9rem;
    color: #7a8aa5;
    margin-bottom: 0.8rem;
}
.ending-desc {
    font-size: 0.95rem;
    line-height: 1.8;
    color: #4a5a72;
    max-width: 480px;
    margin: 0 auto;
}

/* ===== 结论盒子 ===== */
.verdict-box {
    background: linear-gradient(135deg, #fafbfc 0%, #f5f7fa 100%);
    border: 1.5px solid #e2e8f0;
    border-radius: 20px;
    padding: 1.4rem 1.6rem;
    text-align: left;
    margin: 1rem 0;
    color: #2a3441;
    font-size: 0.93rem;
    line-height: 1.8;
    animation: fadeInUp 0.5s ease-out both;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
}

/* ===== 标签样式 ===== */
.tag-pill {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 24px;
    font-size: 0.82rem;
    font-weight: 600;
    margin: 3px;
    transition: all 0.2s ease;
    border: 1.5px solid;
}
.tag-pill:hover {
    transform: scale(1.05);
}

/* ===== 指标卡片 ===== */
.metric-card {
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 16px;
    padding: 1.1rem;
    text-align: center;
    transition: all 0.25s ease;
    animation: fadeInUp 0.4s ease-out both;
}
.metric-card:hover {
    border-color: #c8d4e5;
    transform: translateY(-2px);
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
}
.metric-card .metric-label {
    font-size: 0.72rem;
    color: #7a8aa5;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
}
.metric-card .metric-value {
    font-size: 1.5rem;
    font-weight: 800;
    color: #1e3a5f;
}
.metric-card .metric-delta {
    font-size: 0.78rem;
    font-weight: 600;
    margin-top: 0.2rem;
}
.metric-delta.pos { color: #1e8e52; }
.metric-delta.neg { color: #c0392b; }
.metric-delta.neu { color: #7a8aa5; }

/* ===== 自定义进度条（覆盖 Streamlit 默认） ===== */
[data-testid="stProgress"] {
    height: 38px !important;
    background: #e8ecf3 !important;
    border-radius: 19px !important;
    overflow: hidden !important;
    box-shadow: inset 0 2px 6px rgba(0,0,0,0.06) !important;
    border: 1px solid #d0d8e8 !important;
}
[data-testid="stProgress"] > div:first-child {
    background: transparent !important;
}
[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, #3b6fd8, #2563eb, #3b6fd8) !important;
    background-size: 200% 100% !important;
    animation: shimmer 2s linear infinite !important;
    border-radius: 19px !important;
    height: 100% !important;
}
[data-testid="stProgress"] [data-testid="stMarkdownContainer"] {
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    width: 100% !important;
    text-align: center !important;
    z-index: 10 !important;
}
[data-testid="stProgress"] [data-testid="stMarkdownContainer"] p {
    color: #ffffff !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.06em !important;
    text-shadow: 0 1px 3px rgba(0,0,0,0.25) !important;
    margin: 0 !important;
}

/* ===== 按钮样式 ===== */
[data-testid="stButton"] > button {
    border-radius: 14px !important;
    font-family: 'Noto Sans SC', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    transition: all 0.25s ease !important;
    letter-spacing: 0.02em;
    padding: 0.6rem 1.5rem !important;
}
[data-testid="stButton"] > button[kind="secondary"] {
    background: #ffffff !important;
    border: 2px solid #d0d8e8 !important;
    color: #1e3a5f !important;
}
[data-testid="stButton"] > button[kind="secondary"]:hover {
    background: #f0f4f9 !important;
    border-color: #3b6fd8 !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1) !important;
}
[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    border: none !important;
    color: #ffffff !important;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3) !important;
}
[data-testid="stButton"] > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #3b6fd8, #2563eb) !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4) !important;
}
[data-testid="stButton"] > button:disabled {
    opacity: 0.5 !important;
}

/* ===== 分割线 ===== */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #d0d8e8, transparent);
    margin: 1.5rem 0 !important;
}

/* ===== Alert 修正 ===== */
[data-testid="stAlert"] {
    background: linear-gradient(135deg, #eef4ff, #e6eeff) !important;
    color: #1a2e60 !important;
    border-color: #c8d8f8 !important;
    border-radius: 14px !important;
    font-weight: 600 !important;
}

/* ===== 底部标签行 ===== */
.footer-tags {
    text-align: center;
    margin: 1rem 0;
    font-size: 0.82rem;
    color: #7a8aa5;
    font-weight: 500;
}

/* ===== 选中状态 ===== */
.choice-selected-good {
    border-color: #1e8e52 !important;
    background: linear-gradient(135deg, #edf8f2, #e4f4eb) !important;
    box-shadow: 0 4px 14px rgba(30, 142, 82, 0.15) !important;
}
.choice-selected-bad {
    border-color: #c0392b !important;
    background: linear-gradient(135deg, #fef0f0, #fde8e8) !important;
    box-shadow: 0 4px 14px rgba(192, 57, 43, 0.15) !important;
}

/* ===== 场景标题 ===== */
.scene-header {
    font-size: 1.5rem;
    font-weight: 800;
    color: #1e3a5f;
    letter-spacing: -0.01em;
    margin: 0.5rem 0 0.8rem;
}
.scene-year {
    display: inline-block;
    background: linear-gradient(135deg, #3b6fd8, #2563eb);
    color: white;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 20px;
    margin-right: 0.5rem;
    vertical-align: middle;
    letter-spacing: 0.02em;
}

/* ===== 隐藏 Streamlit 默认元素 ===== */
#MainMenu, footer, header {
    visibility: hidden;
}

/* ===== 滚动条美化 ===== */
::-webkit-scrollbar {
    width: 6px;
}
::-webkit-scrollbar-track {
    background: transparent;
}
::-webkit-scrollbar-thumb {
    background: #c8d4e5;
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
    background: #9aabbf;
}
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
    st.markdown("""
    <div class="main-card" style="text-align:center;padding:2.5rem 2rem;">
        <div class="hero-title">🏢 财务判断室</div>
        <div class="hero-subtitle">科大讯飞研发资本化争议 · 角色扮演</div>
        <hr>
    </div>
    """, unsafe_allow_html=True)

    # 信息卡片
    info_cards = [
        ('🎭', '你的角色', '选择六类真实财务角色之一——管理层、财务人员、审计师、投资者、监管者或债权人。每个角色都有独特的决策视角和压力来源。'),
        ('📌', '游戏情境', '基于科大讯飞真实财务争议，经历三个关键事件节点：星火大模型立项、深交所问询函、定增申请。'),
        ('🎯', '任务目标', '在合规、生存、道德之间做出权衡。没有完美选项，只有取舍。每个选择都会影响最终结局。'),
        ('🏆', '特色机制', '角色专属决策 · 连锁后果 · 多维度评价 · 量化结局 · 真实案例对照'),
    ]

    for icon, title, body in info_cards:
        st.markdown(f"""
        <div class="info-card">
            <div class="info-card-title">{icon} {title}</div>
            <div class="info-card-body">{body}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="footer-tags">游戏时长：8-12分钟 | 超多结局 | 真实职场模拟</div>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown('<h3 style="text-align:center;color:#1e3a5f;font-weight:800;margin:1rem 0 0.5rem;">👇 选择你的角色</h3>', unsafe_allow_html=True)

    # 角色选择卡片
    cols = st.columns(3)
    for i, r in enumerate(ROLES):
        with cols[i % 3]:
            selected = st.session_state.role == r['id']
            card_class = 'role-card selected' if selected else 'role-card'
            st.markdown(f"""
            <div class="{card_class}" style="animation-delay:{i*0.08}s">
                <div class="role-icon">{r['icon']}</div>
                <div class="role-name">{r['name']}</div>
                <div class="role-desc">{r['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"选择{r['name']}", key=f"role_{r['id']}",
                         use_container_width=True,
                         type='primary' if selected else 'secondary'):
                st.session_state.role = r['id']
                st.rerun()

    st.markdown('<hr>', unsafe_allow_html=True)
    if st.session_state.role:
        ri = role_info(st.session_state.role)
        st.info(f"✅ 已选择：{ri['icon']} **{ri['name']}** — {ri['desc']}")
        if st.button('🎮 开始游戏 →', type='primary', use_container_width=True):
            st.session_state.phase = 'scene'
            st.session_state.scene_idx = 0
            st.session_state.scores = []
            st.session_state.chosen = None
            st.session_state.show_feedback = False
            st.rerun()
    else:
        st.button('👆 请先选择角色', disabled=True, use_container_width=True)

# ── SCENE ──
elif st.session_state.phase == 'scene':
    idx = st.session_state.scene_idx
    scene = SCENES[idx]
    role = st.session_state.role
    ri = role_info(role)

    pct = int(((idx + 1) / len(SCENES)) * 100)
    st.markdown(f"""
    <div style="margin:0.6rem 0 1.2rem;">
        <div style="position:relative;height:38px;background:#e8ecf3;border-radius:19px;overflow:hidden;box-shadow:inset 0 2px 6px rgba(0,0,0,0.06);border:1px solid #d0d8e8;">
            <div style="width:{pct}%;height:100%;background:linear-gradient(90deg,#3b6fd8,#2563eb,#3b6fd8);background-size:200% 100%;animation:shimmer 2s linear infinite;border-radius:19px;transition:width 0.6s ease;"></div>
            <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:#ffffff;font-size:0.85rem;font-weight:700;letter-spacing:0.06em;text-shadow:0 1px 3px rgba(0,0,0,0.25);white-space:nowrap;">
                场景 {idx+1} / {len(SCENES)} · {pct}%
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="main-card" style="padding:1.8rem 1.6rem;margin-top:0.8rem;">
        <div class="scene-header">
            <span class="scene-year">{scene['year']}</span>{scene['title']}
        </div>
        <div class="scene-box">{scene['desc']}</div>
    </div>
    """, unsafe_allow_html=True)

    # 指标卡片
    cols = st.columns(3)
    for i, stat in enumerate(scene['stats']):
        delta_class = 'pos' if stat['delta'] and '+' in stat['delta'] else ('neg' if stat['delta'] and '-' in stat['delta'] else 'neu')
        delta_html = f'<div class="metric-delta {delta_class}">{stat["delta"]}</div>' if stat['delta'] else ''
        with cols[i]:
            st.markdown(f"""
            <div class="metric-card" style="animation-delay:{i*0.1}s">
                <div class="metric-label">{stat['label']}</div>
                <div class="metric-value">{stat['value']}</div>
                {delta_html}
            </div>
            """, unsafe_allow_html=True)

    # 视角盒子
    st.markdown(f"""
    <div class="lens-box" style="animation-delay:0.3s">
        <strong>{ri['icon']} {ri['name']}视角：</strong>{scene['lens'][role]}
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<h4 style="color:#1e3a5f;font-weight:800;margin:1.2rem 0 0.6rem;">🤔 你的决策：</h4>', unsafe_allow_html=True)

    choices = scene['role_choices'][role]
    already_chosen = st.session_state.show_feedback
    chosen_idx = st.session_state.chosen

    for i, c in enumerate(choices):
        if already_chosen:
            is_selected = (i == chosen_idx)
            if is_selected:
                score = c['score']
                border_color = '#1e8e52' if score > 0 else ('#c0392b' if score < 0 else '#b07c10')
                bg_color = 'linear-gradient(135deg, #edf8f2, #e4f4eb)' if score > 0 else ('linear-gradient(135deg, #fef0f0, #fde8e8)' if score < 0 else 'linear-gradient(135deg, #fef9ec, #fdf4db)')
                st.markdown(f"""
                <div style="background:{bg_color};border:2.5px solid {border_color};border-radius:16px;padding:1.1rem 1.3rem;margin:0.5rem 0;box-shadow:0 4px 14px {border_color}22;animation:fadeInUp 0.4s ease;">
                    <span style="display:inline-block;background:{border_color};color:white;font-weight:700;width:32px;height:32px;line-height:32px;text-align:center;border-radius:50%;margin-right:0.8rem;vertical-align:top;font-size:0.9rem;">{c['label']}</span>
                    <span style="display:inline-block;font-size:0.92rem;color:#1a2332;line-height:1.6;font-weight:600;">{c['text']}</span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background:#f5f7fa;border:1.5px solid #d8e0ec;border-radius:16px;padding:1.1rem 1.3rem;margin:0.5rem 0;opacity:0.5;">
                    <span style="display:inline-block;background:#c8d4e5;color:white;font-weight:700;width:32px;height:32px;line-height:32px;text-align:center;border-radius:50%;margin-right:0.8rem;vertical-align:top;font-size:0.9rem;">{c['label']}</span>
                    <span style="display:inline-block;font-size:0.92rem;color:#7a8aa5;line-height:1.6;">{c['text']}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            if st.button(f"**{c['label']}.** {c['text']}", key=f'ch_{idx}_{i}',
                         use_container_width=True, type='secondary'):
                st.session_state.chosen = i
                st.session_state.show_feedback = True
                st.session_state.scores.append(c['score'])
                st.rerun()

    if st.session_state.show_feedback and chosen_idx is not None:
        fb = choices[chosen_idx]['feedback']
        st.markdown(f"""
        <div class="feedback-box" style="animation-delay:0.1s">
            <strong>📋 选择结果：</strong><br>{fb}
        </div>
        """, unsafe_allow_html=True)
        st.markdown('')
        is_last = (idx == len(SCENES) - 1)
        if st.button('🏁 查看最终结局 →' if is_last else '➡️ 下一个场景 →',
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

    card_cfg = {
        'good': ('#1e8e52', '#edf8f2', '#0d4a2a'),
        'mid':  ('#b07c10', '#fef9ec', '#5a3e00'),
        'bad':  ('#c0392b', '#fef0f0', '#6b1a1a'),
    }
    accent, bg, text = card_cfg[cat]

    st.markdown(f"""
    <div class="main-card" style="margin-top:1rem;">
        <div class="ending-card" style="background:linear-gradient(135deg, {bg}, #ffffff);border:2px solid {accent}33;">
            <div class="ending-icon">{icon}</div>
            <div class="ending-title" style="color:{accent};">{title}</div>
            <div class="ending-role">{ri['icon']} {ri['name']} 的结局</div>
            <div class="ending-desc" style="color:{text};">{sub}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 得分圆点
    dot_html = ''.join(
        f"<span style='display:inline-block;width:18px;height:18px;border-radius:50%;"
        f"background:{'#1e8e52' if s > 0 else '#c0392b' if s < 0 else '#b07c10'};"
        f"margin:0 6px;box-shadow:0 0 8px {'#1e8e5244' if s > 0 else '#c0392b44' if s < 0 else '#b07c1044'};"
        f"animation:fadeIn 0.3s ease both;animation-delay:{i*0.15}s'></span>"
        for i, s in enumerate(st.session_state.scores)
    )
    st.markdown(f"""
    <div style="text-align:center;margin:1.2rem 0">
        {dot_html}
    </div>
    <div class="footer-tags">🟢 审慎得分 · 🔴 激进失分 · 🟡 中性</div>
    """, unsafe_allow_html=True)

    # 案例对照分析
    st.markdown(f"""
    <div class="verdict-box" style="border-left:5px solid {accent};">
        <p style="font-size:0.75rem;font-weight:700;color:{accent};margin-bottom:0.6rem;text-transform:uppercase;letter-spacing:0.08em;">📋 案例对照分析</p>
        <p style="color:#2a3441;font-size:0.93rem;line-height:1.8;">{VERDICT_TEXT[cat]}</p>
    </div>
    """, unsafe_allow_html=True)

    # 标签
    tag_map = {
        'good': [('✅ 合规导向','#edf8f2','#1e8e52'), ('✅ 职业审慎','#eef3ff','#2255bb'), ('✅ 风险识别','#eef3ff','#2255bb')],
        'mid':  [('⚠️ 压力妥协','#fef9ec','#b07c10'), ('⚠️ 信息不对称','#eef3ff','#2255bb'), ('⚠️ 灰色地带','#fef9ec','#b07c10')],
        'bad':  [('❌ 激进处理','#fef0f0','#c0392b'), ('❌ 利润驱动','#fef0f0','#c0392b'), ('⚠️ 监管风险','#fef9ec','#b07c10')],
    }
    tags_html = ''.join(
        f"<span class='tag-pill' style='background:{bg};color:{fg};border-color:{fg}44;'>"
        f"{t}</span>"
        for t, bg, fg in tag_map[cat]
    )
    st.markdown(f"<div style='margin:1rem 0;text-align:center'>{tags_html}</div>", unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)
    if st.button('🔄 换个角色再玩', use_container_width=True):
        restart()
        st.rerun()
