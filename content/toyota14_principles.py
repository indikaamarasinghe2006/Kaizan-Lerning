# -*- coding: utf-8 -*-
"""
Content module for Study Set 1: The Toyota Way - 14 Management Principles.
Each principle: number, section, title, content (list of paragraphs), questions (10 MCQs).
This file is written in small appended chunks due to length; see build script.
"""

STUDY_SET = {
    "slug": "toyota-14-principles",
    "title": "The Toyota Way: 14 Management Principles",
    "description": (
        "A deep-dive course into the 14 management principles behind the Toyota "
        "Production System, as documented in Jeffrey Liker's 'The Toyota Way'. "
        "Learn the philosophy, process discipline, people-development practices, "
        "and problem-solving culture that made Toyota a global benchmark for "
        "operational excellence."
    ),
}

PRINCIPLES = []

PRINCIPLES.append({
    "number": 1,
    "section": "Section I: Long-Term Philosophy",
    "title": "Base your management decisions on a long-term philosophy, even at the expense of short-term financial goals.",
    "content": [
        "The first principle of the Toyota Way sets the tone for everything that follows: "
        "every decision, from the shop floor to the boardroom, should be anchored in a "
        "long-term sense of purpose rather than the pressure to hit this quarter's numbers. "
        "Toyota describes this as having a 'philosophical mission' that supersedes any "
        "individual manager's tenure — the company exists to create value for customers, "
        "employees, and society over decades, not just to maximize the next earnings report.",

        "This does not mean financial performance is unimportant. Toyota is a highly "
        "profitable company. Rather, it means that profit is treated as the natural "
        "outcome of doing the right things consistently — building quality products, "
        "developing people, and continuously improving processes — rather than as a goal "
        "to be chased directly through shortcuts such as cutting corners on quality, "
        "laying off skilled workers during a downturn, or delaying investment in training.",

        "In practice, a long-term philosophy shows up in decisions like retaining a trained "
        "workforce through a recession instead of laying people off, investing in supplier "
        "relationships that take years to mature, and being willing to absorb a short-term "
        "cost increase to protect a long-term quality or safety standard. Leaders are "
        "expected to be able to explain how a decision serves the organization's purpose "
        "five, ten, or twenty years out — not just how it affects this month's budget.",

        "For an organization adopting this principle, the practical starting point is to "
        "write down and communicate a clear purpose statement that goes beyond profit, and "
        "then to test major decisions against it. When short-term financial pressure and "
        "long-term philosophy conflict, the way that conflict is resolved — and how "
        "transparently it is discussed — reveals whether an organization has genuinely "
        "adopted this principle or only pays it lip service.",
    ],
    "questions": [
        {
            "q": "According to Principle 1, what should be the primary basis for management decisions at Toyota?",
            "options": [
                "Maximizing the next quarterly earnings report",
                "A long-term philosophy, even at the expense of short-term financial goals",
                "Whatever satisfies shareholders fastest",
                "Matching competitors' pricing decisions"
            ],
            "correct": 1,
            "explanation": "Principle 1 explicitly states that decisions should be based on long-term philosophy, even if this means sacrificing short-term financial results."
        },
        {
            "q": "Does Principle 1 imply that Toyota ignores profitability?",
            "options": [
                "Yes, Toyota deliberately avoids being profitable",
                "No, profit is treated as a natural outcome of doing the right things consistently over time",
                "Yes, profitability is only a marketing claim",
                "No, but only government contracts matter"
            ],
            "correct": 1,
            "explanation": "Toyota remains highly profitable; the principle reframes profit as a by-product of long-term, purpose-driven decision-making rather than a short-term target."
        },
        {
            "q": "Which of the following is a real-world example of applying Principle 1?",
            "options": [
                "Laying off trained staff immediately when a quarter's sales dip slightly",
                "Retaining a trained workforce through a downturn instead of quick layoffs",
                "Cutting quality inspection to hit a shipping deadline",
                "Switching suppliers monthly to get the lowest price"
            ],
            "correct": 1,
            "explanation": "Protecting trained talent through short-term downturns reflects a long-term view of workforce value over immediate cost savings."
        },
        {
            "q": "What does Toyota mean by having a 'philosophical mission'?",
            "options": [
                "A mission that changes with every new CEO",
                "A sense of purpose that outlasts any individual manager's tenure",
                "A slogan used only in advertising",
                "A quarterly financial target"
            ],
            "correct": 1,
            "explanation": "The philosophical mission is meant to be enduring and organization-wide, not tied to a single leader's term or a single financial cycle."
        },
        {
            "q": "How should leaders justify major decisions under Principle 1?",
            "options": [
                "By showing the effect on this month's budget only",
                "By explaining how the decision serves the organization's purpose years into the future",
                "By comparing it only to competitor actions",
                "By avoiding any explanation to staff"
            ],
            "correct": 1,
            "explanation": "Leaders are expected to connect decisions to the long-term purpose of the organization, not just immediate financial impact."
        },
        {
            "q": "What reveals whether an organization has truly adopted Principle 1, according to the material?",
            "options": [
                "How much revenue it earns in a single year",
                "How it resolves conflicts between short-term financial pressure and long-term philosophy",
                "The number of principles it lists on its website",
                "How many press releases it issues"
            ],
            "correct": 1,
            "explanation": "The real test of this principle is visible when short-term and long-term interests conflict and the organization must choose."
        },
        {
            "q": "Which stakeholder group is explicitly mentioned as part of the long-term purpose beyond shareholders?",
            "options": [
                "Employees and society",
                "Only competitors",
                "Only government regulators",
                "Only short-term investors"
            ],
            "correct": 0,
            "explanation": "The long-term philosophy is meant to create value for customers, employees, and society — not just shareholders."
        },
        {
            "q": "What is a practical first step for an organization trying to adopt Principle 1?",
            "options": [
                "Eliminate all long-range planning meetings",
                "Write and communicate a clear purpose statement beyond profit, then test decisions against it",
                "Focus solely on beating this year's budget",
                "Outsource all strategic decisions to consultants"
            ],
            "correct": 1,
            "explanation": "A documented, communicated purpose gives leaders a concrete standard to test decisions against."
        },
        {
            "q": "Investing in supplier relationships that take years to mature is an example of which idea in Principle 1?",
            "options": [
                "Short-term cost minimization",
                "Long-term value creation over immediate savings",
                "Avoiding all supplier partnerships",
                "Quarterly contract renegotiation"
            ],
            "correct": 1,
            "explanation": "Long-maturing supplier relationships are a long-term investment consistent with Principle 1's philosophy."
        },
        {
            "q": "Which statement best summarizes Principle 1 for a new manager joining Toyota?",
            "options": [
                "Chase short-term wins whenever possible",
                "Let long-term purpose guide decisions, even when it costs more right now",
                "Ignore financial results entirely",
                "Only follow instructions from headquarters without question"
            ],
            "correct": 1,
            "explanation": "This captures the core idea: purpose-driven, long-term thinking guides decisions even when it is costlier in the short run."
        }
    ]
})

PRINCIPLES.append({
    "number": 2,
    "section": "Section II: The Right Process Will Produce the Right Results",
    "title": "Create continuous process flow to bring problems to the surface.",
    "content": [
        "Principle 2 asks organizations to redesign work so that material and information "
        "move in a smooth, uninterrupted flow from one process step to the next, rather than "
        "sitting in large batches or queues between departments. When work flows continuously, "
        "there is nowhere for a defect, delay, or bottleneck to hide — problems surface almost "
        "immediately, at the point where they are cheapest and easiest to fix.",

        "Traditional batch-and-queue production optimizes each department in isolation: a "
        "machine runs a huge batch to maximize its own utilization, then the batch waits in "
        "storage before the next department is ready. This hides problems for weeks — a "
        "quality issue introduced early in the batch might not be discovered until the whole "
        "batch reaches final inspection, by which point hundreds of defective units already "
        "exist and the root cause is hard to trace.",

        "Toyota's answer is to link processes tightly together, often through single-piece or "
        "small-lot flow, so that each unit moves to the next step as soon as it is ready. If a "
        "problem occurs, the line stops or slows almost immediately, forcing the team to "
        "confront and resolve it on the spot instead of stockpiling problems for later. This "
        "requires reliable equipment, well-trained operators, and processes stable enough to "
        "run without constant firefighting — which is why flow is described as revealing "
        "problems rather than causing them.",

        "Creating flow is uncomfortable at first because it removes the buffers that "
        "traditionally hide inefficiency, variability, and quality issues. Organizations "
        "adopting this principle typically start by mapping their current value stream, "
        "identifying where work piles up in queues, and redesigning the physical or digital "
        "layout so work items move step-by-step with minimal waiting, making problems visible "
        "the moment they occur.",
    ],
    "questions": [
        {
            "q": "What is the primary purpose of creating continuous process flow under Principle 2?",
            "options": [
                "To maximize the utilization of each individual machine",
                "To bring problems to the surface quickly so they can be fixed",
                "To build the largest possible inventory buffer",
                "To reduce the number of employees needed"
            ],
            "correct": 1,
            "explanation": "Continuous flow removes hiding places for problems, exposing them immediately rather than letting them accumulate."
        },
        {
            "q": "In traditional batch-and-queue production, when might a quality defect typically be discovered?",
            "options": [
                "Immediately at the exact workstation where it occurred",
                "Potentially weeks later, once the whole batch reaches final inspection",
                "Before the batch even starts",
                "Only during annual audits"
            ],
            "correct": 1,
            "explanation": "Batches can sit and move as a whole, so a defect introduced early may not surface until the entire batch is inspected much later."
        },
        {
            "q": "What typically happens on a Toyota-style flow line when a problem occurs?",
            "options": [
                "The batch keeps moving regardless of the problem",
                "The line stops or slows so the team can resolve the issue immediately",
                "The defective unit is quietly discarded without investigation",
                "Production is paused for a full week"
            ],
            "correct": 1,
            "explanation": "Flow is designed so that a problem causes an immediate, visible interruption, prompting quick resolution."
        },
        {
            "q": "What does continuous flow require from equipment and processes to work well?",
            "options": [
                "Constant firefighting and improvisation",
                "Reliability and enough stability to run without frequent breakdowns",
                "Large amounts of buffer inventory between every step",
                "Minimal operator training"
            ],
            "correct": 1,
            "explanation": "Flow depends on stable, reliable processes; without this, frequent stoppages would make flow impractical."
        },
        {
            "q": "Why is single-piece or small-lot flow preferred over large-batch processing under this principle?",
            "options": [
                "It hides problems for longer, which is desirable",
                "It lets each unit move on quickly so issues are caught close to when they occur",
                "It requires no changes to layout or process",
                "It always requires more inventory"
            ],
            "correct": 1,
            "explanation": "Smaller lot sizes shorten the distance (in time and units) between a problem occurring and it being detected."
        },
        {
            "q": "What is a common first step organizations take when adopting Principle 2?",
            "options": [
                "Immediately eliminate all quality inspections",
                "Map the current value stream to find where work piles up in queues",
                "Increase batch sizes to reduce changeovers",
                "Move all production offshore"
            ],
            "correct": 1,
            "explanation": "Value stream mapping helps identify queues and delays that need to be redesigned into flow."
        },
        {
            "q": "Why might creating flow feel uncomfortable at first for an organization?",
            "options": [
                "It adds more inventory buffers to hide problems",
                "It removes buffers that previously hid inefficiency and variability",
                "It requires no changes to daily operations",
                "It guarantees zero problems immediately"
            ],
            "correct": 1,
            "explanation": "Removing buffers exposes issues that were previously hidden, which can feel disruptive before it becomes beneficial."
        },
        {
            "q": "Which best describes the relationship between flow and problem visibility?",
            "options": [
                "Flow hides problems more effectively than batching",
                "Flow exposes problems close to where and when they occur",
                "Flow and problem visibility are unrelated",
                "Flow only applies to office work, not manufacturing"
            ],
            "correct": 1,
            "explanation": "The core benefit of flow is that it makes problems visible almost as soon as they happen."
        },
        {
            "q": "In batch production, why can it be hard to trace the root cause of a defect found at final inspection?",
            "options": [
                "Because defects in batches are always intentional",
                "Because many units and process steps have passed since the defect was introduced",
                "Because root cause analysis is unnecessary in batch systems",
                "Because batch systems never produce defects"
            ],
              "correct": 1,
            "explanation": "By the time a batch reaches inspection, tracing back to the exact point and cause of the defect is much harder."
        },
        {
            "q": "What is the ultimate goal of applying Principle 2 across an organization's processes?",
            "options": [
                "To isolate departments from one another as much as possible",
                "To tightly link process steps so work — and problems — move visibly and quickly",
                "To maximize work-in-process inventory",
                "To eliminate the need for teamwork"
            ],
            "correct": 1,
            "explanation": "Continuous flow links steps together so material and problems move visibly, supporting fast detection and resolution."
        }
    ]
})

PRINCIPLES.append({
    "number": 3,
    "section": "Section II: The Right Process Will Produce the Right Results",
    "title": "Use 'pull' systems to avoid overproduction.",
    "content": [
        "Principle 3 introduces the idea of a pull system, where downstream processes signal "
        "upstream processes to produce or deliver only what is needed, exactly when it is "
        "needed, and in the amount needed. This stands in direct contrast to a 'push' system, "
        "where each step produces as much as it can and pushes the output forward regardless "
        "of whether the next step is ready to use it.",

        "Overproduction is considered the most serious of the seven classic wastes in the "
        "Toyota Production System because it creates all the other wastes: excess inventory, "
        "extra transportation and storage, higher risk of defects going unnoticed, and capital "
        "tied up in goods nobody has asked for yet. A pull system directly attacks "
        "overproduction by making replenishment conditional on actual consumption.",

        "The most well-known tool for implementing pull is the kanban card or signal, which "
        "travels with a container of parts and authorizes the upstream process to make a "
        "replacement only once that container has been consumed downstream. This creates a "
        "tight, visible link between supply and actual demand, so inventory naturally settles "
        "at the minimum level needed to keep the flow running smoothly.",

        "Adopting pull requires trust and discipline: upstream processes must resist the "
        "temptation to run large batches for efficiency and instead produce in small "
        "increments triggered by real signals. In return, the organization gains lower "
        "inventory carrying costs, faster response to changes in actual customer demand, and "
        "a system where nobody has to guess how much to produce far in advance.",
    ],
    "questions": [
        {
            "q": "What is a 'pull' system designed to do, according to Principle 3?",
            "options": [
                "Produce as much as possible ahead of demand",
                "Have downstream processes signal upstream processes to produce only what is needed, when needed",
                "Eliminate the need for any communication between processes",
                "Increase inventory buffers at every stage"
            ],
            "correct": 1,
            "explanation": "Pull systems replenish based on actual downstream consumption rather than forecasts or upstream convenience."
        },
        {
            "q": "Why is overproduction considered the most serious of the classic wastes?",
            "options": [
                "It has no effect on other forms of waste",
                "It creates or amplifies most other wastes, such as excess inventory and hidden defects",
                "It is the cheapest waste to correct",
                "It only affects marketing departments"
            ],
            "correct": 1,
            "explanation": "Overproduction drives excess inventory, storage, transportation, and can hide quality problems, making it foundational to many other wastes."
        },
        {
            "q": "What is a kanban in the context of a pull system?",
            "options": [
                "A financial report used only by executives",
                "A card or signal that authorizes replenishment once material has been consumed downstream",
                "A type of overproduction",
                "A quality certificate issued to suppliers"
            ],
            "correct": 1,
            "explanation": "Kanban signals link supply to actual demand, authorizing production or replenishment only after consumption occurs."
        },
        {
            "q": "How does a push system differ from a pull system?",
            "options": [
                "A push system waits for downstream signals before producing",
                "A push system produces based on upstream capacity/plans regardless of downstream readiness",
                "A push system and pull system are identical in practice",
                "A push system only exists in service industries"
            ],
            "correct": 1,
            "explanation": "Push systems move output forward based on upstream schedules, not real downstream consumption, unlike pull systems."
        },
        {
            "q": "What does a pull system require from upstream processes?",
            "options": [
                "Running the largest possible batches regardless of demand",
                "Discipline to produce in small increments triggered by real consumption signals",
                "Ignoring downstream requests entirely",
                "Eliminating all communication with downstream teams"
            ],
            "correct": 1,
            "explanation": "Upstream teams must resist large-batch efficiency thinking and instead respond to actual pull signals."
        },
        {
            "q": "What benefit does a pull system provide regarding inventory levels?",
            "options": [
                "It maximizes inventory at every process step",
                "Inventory naturally settles near the minimum needed to sustain flow",
                "It has no effect on inventory levels",
                "It requires doubling safety stock permanently"
            ],
            "correct": 1,
            "explanation": "Because replenishment matches actual consumption, inventory tends to stabilize at low, needed levels."
        },
        {
            "q": "Which of these is a hidden risk of overproduction mentioned in the material?",
            "options": [
                "Defects going unnoticed within large unused inventories",
                "Immediate detection of every defect",
                "Reduced capital tied up in goods",
                "Faster customer response times"
            ],
            "correct": 0,
            "explanation": "When large quantities are produced ahead of need, defects can remain hidden within stockpiles for longer periods."
        },
        {
            "q": "What does adopting a pull system ultimately allow an organization to respond better to?",
            "options": [
                "Forecast errors made a year in advance",
                "Actual, real-time customer demand",
                "Only internal production quotas",
                "Competitor advertising campaigns"
            ],
            "correct": 1,
            "explanation": "Pull systems are tied to real consumption, making them responsive to actual demand rather than forecasts."
        },
        {
            "q": "What must an organization trust in order to successfully implement a pull system?",
            "options": [
                "That upstream processes will produce as much as possible regardless of signals",
                "That the signal-based replenishment process will work without needing large safety buffers",
                "That downstream demand is irrelevant",
                "That no communication between processes is needed"
            ],
            "correct": 1,
            "explanation": "Trust in the pull mechanism itself — rather than relying on large buffers — is essential to make the system work."
        },
        {
            "q": "Which outcome is NOT a benefit of pull systems described in the material?",
            "options": [
                "Lower inventory carrying costs",
                "Faster response to actual demand changes",
                "Guessing far in advance how much to produce",
                "A tighter, visible link between supply and demand"
            ],
            "correct": 2,
            "explanation": "Pull systems specifically remove the need to guess production quantities far in advance, unlike forecast-driven push systems."
        }
    ]
})

PRINCIPLES.append({
    "number": 4,
    "section": "Section II: The Right Process Will Produce the Right Results",
    "title": "Level out the workload (Heijunka).",
    "content": [
        "Heijunka, or production leveling, means smoothing out both the volume and the mix of "
        "work over time instead of producing in large, uneven batches that swing between "
        "extremes of overload and idleness. Rather than building all of one product on Monday "
        "and all of another on Tuesday, a leveled schedule interweaves smaller amounts of each "
        "product throughout every day, creating a steady, predictable rhythm of work.",

        "Toyota identifies three types of waste that leveling helps address, known by their "
        "Japanese terms: muda (non-value-added waste), muri (overburden of people or "
        "equipment), and mura (unevenness). Unevenness, mura, is often the root cause of the "
        "other two — when demand on a process spikes and dips unpredictably, it forces periods "
        "of overburden (muri) followed by periods of idle waste (muda). Leveling attacks mura "
        "directly, which in turn reduces the pressure that creates the other two wastes.",

        "A leveled schedule also makes an organization far more resilient to demand "
        "variability. Because work is spread evenly, machines, workers, and suppliers can plan "
        "around a stable rhythm rather than constantly reacting to feast-or-famine ordering "
        "patterns. This stability is also what allows small-lot, pull-based flow (Principles 2 "
        "and 3) to work reliably, since wildly fluctuating batch sizes would overwhelm a "
        "tightly linked flow system.",

        "Implementing heijunka typically involves smoothing the final assembly schedule first, "
        "using tools such as a heijunka box that sequences small batches of different product "
        "variants in a fixed, repeating pattern, and then working backward to level supplier "
        "deliveries and upstream processes to match. It requires short changeover times, since "
        "producing a greater variety of smaller batches only works economically if switching "
        "between them is fast and low-cost.",
    ],
    "questions": [
        {
            "q": "What does 'heijunka' mean in the context of Principle 4?",
            "options": [
                "Producing in the largest batches possible",
                "Leveling out the volume and mix of production over time",
                "Eliminating all product variety",
                "Increasing overtime hours indefinitely"
            ],
            "correct": 1,
            "explanation": "Heijunka is about smoothing both how much and what mix of products are produced, avoiding uneven spikes and troughs."
        },
        {
            "q": "Which three types of waste does the material associate with leveling?",
            "options": [
                "Muda, muri, and mura",
                "Kaizen, kanban, and jidoka",
                "Genchi genbutsu, hansei, and nemawashi",
                "Push, pull, and flow"
            ],
            "correct": 0,
            "explanation": "Muda (non-value-added waste), muri (overburden), and mura (unevenness) are the three wastes leveling addresses."
        },
        {
            "q": "According to the material, which of the three wastes is often the root cause of the other two?",
            "options": [
                "Muda",
                "Muri",
                "Mura (unevenness)",
                "None of them are related"
            ],
            "correct": 2,
            "explanation": "Unevenness (mura) tends to create alternating overburden (muri) and idle waste (muda), so addressing mura reduces both."
        },
        {
            "q": "What is a heijunka box used for?",
            "options": [
                "Storing finished goods indefinitely",
                "Sequencing small batches of different product variants in a fixed, repeating pattern",
                "Recording customer complaints",
                "Tracking employee attendance"
            ],
            "correct": 1,
            "explanation": "A heijunka box is a scheduling tool that visually sequences a leveled mix of production."
        },
        {
            "q": "Why does leveling make an organization more resilient to demand variability?",
            "options": [
                "Because it eliminates the need for suppliers",
                "Because a stable, predictable rhythm lets people and machines plan around consistent workload",
                "Because it guarantees demand never changes",
                "Because it increases unpredictable overtime"
            ],
            "correct": 1,
            "explanation": "A steady rhythm reduces the shocks of feast-or-famine demand swings, aiding planning and stability."
        },
        {
            "q": "What must be true of changeover times for heijunka to work economically with smaller, varied batches?",
            "options": [
                "Changeovers must be slow and costly",
                "Changeovers must be short and low-cost",
                "Changeovers are irrelevant to heijunka",
                "Only one product variant can ever be made"
            ],
            "correct": 1,
            "explanation": "Fast, cheap changeovers make it feasible to produce a greater variety of smaller batches without losing efficiency."
        },
        {
            "q": "How does heijunka support the pull and flow principles (2 and 3)?",
            "options": [
                "It destabilizes flow by increasing batch size swings",
                "It provides the stable rhythm that tightly linked flow and pull systems need to function reliably",
                "It has no relationship to flow or pull",
                "It replaces the need for pull systems entirely"
            ],
            "correct": 1,
            "explanation": "Flow and pull systems depend on predictable, steady work patterns, which leveling provides."
        },
        {
            "q": "What is typically leveled first when implementing heijunka in a plant?",
            "options": [
                "Executive travel schedules",
                "The final assembly schedule",
                "Marketing budgets",
                "Customer complaint logs"
            ],
            "correct": 1,
            "explanation": "Leveling usually starts at final assembly and then works backward to align supplier and upstream process schedules."
        },
        {
            "q": "What happens to workers and equipment when demand is NOT leveled, according to the material?",
            "options": [
                "They experience a perfectly steady workload",
                "They alternate between overburden (muri) during spikes and idle waste (muda) during lulls",
                "They are unaffected by demand swings",
                "They automatically level the schedule themselves"
            ],
            "correct": 1,
            "explanation": "Unleveled demand creates alternating overload and idleness for people and equipment."
        },
        {
            "q": "Which best captures the overall goal of Principle 4?",
            "options": [
                "Maximize batch size to reduce changeovers",
                "Create a steady, predictable rhythm of mixed production to reduce unevenness and its downstream effects",
                "Randomize the production schedule to keep workers alert",
                "Only produce one product at a time, in huge quantities"
            ],
            "correct": 1,
            "explanation": "Heijunka aims for a steady, mixed, predictable production rhythm that minimizes mura and its consequences."
        }
    ]
})

PRINCIPLES.append({
    "number": 5,
    "section": "Section II: The Right Process Will Produce the Right Results",
    "title": "Build a culture of stopping to fix problems, to get quality right the first time (Jidoka).",
    "content": [
        "Jidoka is often translated as 'automation with a human touch.' It refers to designing "
        "machines and processes so that they can detect an abnormality and stop automatically, "
        "and equally important, empowering every worker with the authority — and the "
        "expectation — to stop the line the moment they spot a defect or problem, rather than "
        "letting it pass downstream.",

        "The visible symbol of this principle at Toyota is the andon cord: a physical cord or "
        "button that any team member can pull to signal a problem, which can halt the "
        "production line if the issue is not resolved quickly. This is a radical departure "
        "from traditional mass production, where stopping the line was treated as a costly "
        "failure to be avoided at almost any price, even if it meant shipping defects forward.",

        "Quality built in at the source is far cheaper than quality inspected in afterward. "
        "When a problem is caught and fixed at the exact station and moment it occurs, the fix "
        "is simple and the root cause is fresh and traceable. When the same problem is instead "
        "discovered at final inspection or, worse, by a customer, the cost of correction "
        "multiplies many times over, and the true root cause may never be found.",

        "Building a jidoka culture requires courage from leadership: line stoppages must be "
        "treated as valuable opportunities to learn and improve, not as reasons to punish the "
        "person who pulled the cord. Over time, organizations that embrace this principle see "
        "stoppages become rarer, not because problems are being hidden again, but because root "
        "causes are being permanently eliminated one by one.",
    ],
    "questions": [
        {
            "q": "How is jidoka often translated?",
            "options": [
                "Automation with a human touch",
                "Total elimination of all machines",
                "Maximum production speed",
                "Continuous financial reporting"
            ],
            "correct": 0,
            "explanation": "Jidoka combines automatic problem detection in machines with human authority to stop and fix issues."
        },
        {
            "q": "What is the andon cord used for?",
            "options": [
                "Ordering raw materials",
                "Allowing any team member to signal a problem and potentially stop the line",
                "Recording employee attendance",
                "Communicating only with senior executives"
            ],
            "correct": 1,
            "explanation": "The andon cord empowers workers to halt production immediately when they detect a defect or issue."
        },
        {
            "q": "How does jidoka's approach to line stoppages differ from traditional mass production?",
            "options": [
                "Traditional mass production encourages frequent line stops",
                "Traditional mass production treats stopping the line as a costly failure to avoid at almost any cost",
                "Jidoka forbids ever stopping the line",
                "There is no difference between the two approaches"
            ],
            "correct": 1,
            "explanation": "Traditional mass production often prioritized keeping the line running over stopping for quality issues, unlike jidoka."
        },
        {
            "q": "Why is quality built in at the source considered cheaper than inspecting afterward?",
            "options": [
                "Because problems caught immediately are simpler to fix and the root cause is still fresh",
                "Because inspection afterward always costs less",
                "Because building in quality requires no changes to process",
                "Because customers prefer to find defects themselves"
            ],
            "correct": 0,
            "explanation": "Catching and fixing issues at the point of occurrence keeps root causes traceable and fixes simple, unlike late-stage detection."
        },
        {
            "q": "What happens to the cost of correcting a defect if it reaches the customer instead of being caught at the source?",
            "options": [
                "It stays exactly the same",
                "It decreases significantly",
                "It multiplies many times over",
                "It becomes irrelevant"
            ],
            "correct": 2,
            "explanation": "The later a defect is caught, the more expensive and complex it becomes to correct, especially once it reaches customers."
        },
        {
            "q": "What kind of leadership behavior does a genuine jidoka culture require?",
            "options": [
                "Punishing workers who pull the andon cord",
                "Treating line stoppages as valuable learning and improvement opportunities",
                "Discouraging any reporting of problems",
                "Removing the andon system after repeated use"
            ],
            "correct": 1,
            "explanation": "Leaders must support stoppages as opportunities to fix root causes, not as failures to be punished."
        },
        {
            "q": "Over time, what typically happens to the frequency of line stoppages in a mature jidoka culture?",
            "options": [
                "Stoppages increase indefinitely with no benefit",
                "Stoppages become rarer as root causes are permanently eliminated",
                "Stoppages stay exactly the same forever",
                "Stoppages are hidden from management"
            ],
            "correct": 1,
            "explanation": "As root causes get fixed permanently, the underlying problems that trigger stoppages become less frequent."
        },
        {
            "q": "Which best describes the human element of jidoka?",
            "options": [
                "Only engineers are allowed to stop the line",
                "Every worker is empowered and expected to stop the line when they spot a defect",
                "Workers are discouraged from noticing defects",
                "Only automated systems can detect problems, humans have no role"
            ],
            "correct": 1,
            "explanation": "Jidoka gives every worker, not just engineers or machines, the authority to halt production over a quality issue."
        },
        {
            "q": "What does it mean for a machine to have 'built-in' jidoka capability?",
            "options": [
                "It can detect an abnormality and stop automatically",
                "It runs continuously regardless of defects",
                "It requires constant human supervision to notice any issue",
                "It cannot be stopped under any circumstances"
            ],
            "correct": 0,
            "explanation": "Jidoka-enabled machines are designed to sense abnormal conditions and stop themselves without needing a human to notice first."
        },
        {
            "q": "What is the underlying goal of Principle 5?",
            "options": [
                "To maximize output regardless of defects",
                "To get quality right the first time by stopping and fixing problems immediately",
                "To hide problems from customers as long as possible",
                "To eliminate all human involvement in quality control"
            ],
            "correct": 1,
            "explanation": "Principle 5 is fundamentally about building quality in at the source rather than inspecting it in afterward."
        }
    ]
})

PRINCIPLES.append({
    "number": 6,
    "section": "Section II: The Right Process Will Produce the Right Results",
    "title": "Standardized tasks are the foundation for continuous improvement and employee empowerment.",
    "content": [
        "Standardized work means documenting the current best-known way to perform a task — "
        "the sequence of steps, the takt time, and the expected outcome — so that every person "
        "doing that job does it the same, proven way. Far from being rigid or bureaucratic, "
        "Toyota treats standards as the essential baseline from which improvement is measured "
        "and made possible.",

        "Without a standard, there is no reliable way to know whether a change to a process is "
        "actually an improvement, because there is no consistent 'before' to compare it "
        "against. A documented standard makes deviations, defects, and inefficiencies "
        "immediately visible, because anyone can compare what is actually happening to what "
        "should be happening according to the agreed standard.",

        "Critically, standards at Toyota are not handed down permanently from management — "
        "they are created with input from the people who actually do the work, and they are "
        "expected to change as better methods are discovered through kaizen. Standardized work "
        "is therefore described as 'the current best known way,' not the final or only way, "
        "and every worker is encouraged and expected to propose improvements to it.",

        "This creates a virtuous cycle of empowerment: because workers understand exactly what "
        "the standard is and why it exists, they can spot when something is off and are "
        "trusted to raise or fix it, and because they helped shape the standard, they take "
        "ownership of following it and improving it further. Standardization and continuous "
        "improvement are therefore not opposites — one enables the other.",
    ],
    "questions": [
        {
            "q": "What does standardized work document, according to Principle 6?",
            "options": [
                "Only the final output quality checklist",
                "The current best-known sequence of steps, takt time, and expected outcome for a task",
                "A permanent, unchangeable set of rules",
                "Only management's preferences, ignoring workers' input"
            ],
            "correct": 1,
            "explanation": "Standardized work captures the best current method, including sequence, timing, and expected results."
        },
        {
            "q": "Why does Toyota consider standards essential for continuous improvement?",
            "options": [
                "Standards prevent any changes from ever happening",
                "Without a consistent baseline, it's impossible to reliably tell if a change is truly an improvement",
                "Standards are unrelated to improvement efforts",
                "Standards eliminate the need for measurement"
            ],
            "correct": 1,
            "explanation": "A standard provides the 'before' state needed to judge whether a proposed change is actually better."
        },
        {
            "q": "Who is typically involved in creating standards at Toyota?",
            "options": [
                "Only senior executives, with no worker input",
                "The people who actually perform the work",
                "External consultants exclusively",
                "No one — standards are generated automatically"
            ],
            "correct": 1,
            "explanation": "Standards are built with input from the workers who do the job, increasing accuracy and buy-in."
        },
        {
            "q": "How does Toyota describe standardized work in terms of permanence?",
            "options": [
                "As the final, unchangeable way to do a task forever",
                "As 'the current best known way,' expected to evolve through kaizen",
                "As irrelevant once written down",
                "As something only used once during onboarding"
            ],
            "correct": 1,
            "explanation": "Standards are living documents meant to be updated as better methods are discovered."
        },
        {
            "q": "How does a documented standard help make problems visible?",
            "options": [
                "It hides deviations from view",
                "It gives a clear reference so anyone can compare actual work to what should be happening",
                "It removes the need for any comparison",
                "It only applies to management reports"
            ],
            "correct": 1,
            "explanation": "A clear standard makes it obvious when actual performance deviates from the expected method."
        },
        {
            "q": "Why are standardization and continuous improvement described as complementary, not opposites?",
            "options": [
                "Because standards block all future improvement",
                "Because a stable standard provides the baseline needed to measure and drive improvement",
                "Because they have nothing to do with each other",
                "Because improvement only happens without any standards"
            ],
            "correct": 1,
            "explanation": "Standards and kaizen work together: standards create the baseline, and kaizen improves upon it, then a new standard is set."
        },
        {
            "q": "What does worker involvement in creating standards tend to produce?",
            "options": [
                "Resentment and lower compliance",
                "Greater ownership and willingness to follow and improve the standard",
                "No measurable effect on behavior",
                "Complete rejection of all standards"
            ],
            "correct": 1,
            "explanation": "When workers help shape standards, they tend to feel more ownership over following and improving them."
        },
        {
            "q": "What is a takt time, as referenced in standardized work?",
            "options": [
                "A random time interval with no production meaning",
                "The expected pace or timing at which a task should be completed to match demand",
                "The time it takes to hire a new employee",
                "A financial reporting period"
            ],
            "correct": 1,
            "explanation": "Takt time is part of a standard describing the expected pace of work aligned with customer demand."
        },
        {
            "q": "What role are workers expected to play regarding existing standards?",
            "options": [
                "Follow them blindly forever with no feedback",
                "Follow them as the current best method while proposing improvements when better methods are found",
                "Ignore them whenever convenient",
                "Only follow standards set by external auditors"
            ],
            "correct": 1,
            "explanation": "Workers follow the current standard but are encouraged to suggest and help implement improvements over time."
        },
        {
            "q": "What is the foundational idea behind Principle 6?",
            "options": [
                "Standards are bureaucratic obstacles with no value",
                "Standardized tasks provide the stable foundation needed for both improvement and empowerment",
                "Only management should understand the standards",
                "Standards should never be written down"
            ],
            "correct": 1,
            "explanation": "Principle 6 frames standardization as the enabling foundation for both continuous improvement and empowering workers."
        }
    ]
})

PRINCIPLES.append({
    "number": 7,
    "section": "Section II: The Right Process Will Produce the Right Results",
    "title": "Use visual control so no problems are hidden.",
    "content": [
        "Principle 7 calls for organizing the workplace so that its status can be understood at "
        "a glance, without needing to ask anyone or dig through a report. This includes simple "
        "devices such as andon boards that show line status in real time, shadow boards that "
        "make a missing tool immediately obvious, color-coded floor markings that show where "
        "material belongs, and kanban cards that visually signal replenishment needs.",

        "The underlying philosophy borrows from the 5S methodology — Sort, Set in order, "
        "Shine, Standardize, and Sustain — which creates a clean, organized, and visually "
        "self-explanatory workplace. When everything has an obvious place and an obvious "
        "normal state, any abnormality (a missing part, a misplaced tool, a stalled process) "
        "stands out immediately to anyone walking by, not just to a specialist who knows where "
        "to look.",

        "Visual control extends beyond the factory floor into offices and management systems: "
        "large visible charts tracking key metrics, color-coded status boards for projects, and "
        "simple one-page reports replace thick binders and buried spreadsheets. The goal is the "
        "same everywhere — make performance and problems visible enough that management by "
        "walking around is genuinely effective, rather than relying on delayed or filtered "
        "reports.",

        "Effective visual controls are simple, intuitive, and require little or no training to "
        "interpret. If a system requires a manual to understand, it has failed as a visual "
        "control. The test of a good visual system is whether a visitor unfamiliar with the "
        "process can look at it and immediately tell whether things are running normally or "
        "not.",
    ],
    "questions": [
        {
            "q": "What is the primary goal of visual control under Principle 7?",
            "options": [
                "To make workplace status understandable at a glance, without needing to ask anyone",
                "To hide problems from visitors",
                "To replace all human judgment with software",
                "To increase the amount of paperwork required"
            ],
            "correct": 0,
            "explanation": "Visual control aims for instant, at-a-glance understanding of status and problems."
        },
        {
            "q": "Which methodology is described as underlying much of visual workplace organization?",
            "options": [
                "Six Sigma DMAIC",
                "5S (Sort, Set in order, Shine, Standardize, Sustain)",
                "SWOT analysis",
                "Balanced Scorecard"
            ],
            "correct": 1,
            "explanation": "5S creates the clean, organized, self-explanatory environment that visual controls depend on."
        },
        {
            "q": "What is a shadow board used for?",
            "options": [
                "Tracking financial performance",
                "Making a missing tool immediately obvious by outlining where it belongs",
                "Recording customer feedback",
                "Scheduling employee shifts"
            ],
            "correct": 1,
            "explanation": "A shadow board visually marks each tool's location so a missing tool is instantly noticeable."
        },
        {
            "q": "According to the material, what is the test of a good visual control system?",
            "options": [
                "Whether it requires a detailed manual to interpret",
                "Whether a visitor unfamiliar with the process can immediately tell if things are normal or not",
                "Whether only senior managers can understand it",
                "Whether it hides abnormalities from view"
            ],
            "correct": 1,
            "explanation": "Good visual controls are self-explanatory enough for anyone to interpret at a glance."
        },
        {
            "q": "How does visual control support 'management by walking around'?",
            "options": [
                "By making performance and problems visible enough to assess without delayed reports",
                "By eliminating the need for managers to visit the workplace",
                "By requiring managers to read lengthy spreadsheets first",
                "By hiding project status from managers"
            ],
            "correct": 0,
            "explanation": "When status is visible directly on the floor or in simple charts, managers can assess situations directly and immediately."
        },
        {
            "q": "Which of these is an example of visual control mentioned in the material?",
            "options": [
                "A thick binder of quarterly reports",
                "An andon board showing real-time line status",
                "A private email sent only to executives",
                "A verbal-only handoff between shifts"
            ],
            "correct": 1,
            "explanation": "Andon boards are a classic example of real-time, visible status indicators."
        },
        {
            "q": "What happens to abnormalities in a well-organized visual workplace?",
            "options": [
                "They blend in and go unnoticed",
                "They stand out immediately because everything has an obvious normal state",
                "They require a specialist to detect",
                "They are only discovered during annual audits"
            ],
            "correct": 1,
            "explanation": "When normal conditions are visually obvious, deviations from normal are easy to spot immediately."
        },
        {
            "q": "How does Principle 7 apply outside the factory floor?",
            "options": [
                "It does not apply outside manufacturing at all",
                "Through visible charts, color-coded status boards, and simple one-page reports in offices",
                "Only through verbal briefings with no visual aids",
                "By eliminating all reporting entirely"
            ],
            "correct": 1,
            "explanation": "Visual management extends to office and administrative settings through simple, visible tracking tools."
        },
        {
            "q": "What does it mean if a visual control system requires a manual to understand?",
            "options": [
                "It is functioning as intended",
                "It has failed as a visual control",
                "It should be used only by new employees",
                "It should replace all other communication"
            ],
            "correct": 1,
            "explanation": "Effective visual controls should be intuitive; needing a manual defeats the purpose of instant clarity."
        },
        {
            "q": "What is the overarching purpose of Principle 7 within the Toyota Way?",
            "options": [
                "To ensure no problems are hidden by making the workplace visually self-explanatory",
                "To centralize all information exclusively with top management",
                "To reduce workplace organization efforts",
                "To replace standardized work with visual guesswork"
            ],
            "correct": 0,
            "explanation": "The title of Principle 7 itself states the goal: use visual control so no problems are hidden."
        }
    ]
})

PRINCIPLES.append({
    "number": 8,
    "section": "Section II: The Right Process Will Produce the Right Results",
    "title": "Use only reliable, thoroughly tested technology that serves your people and processes.",
    "content": [
        "Principle 8 addresses how an organization should approach new technology: not by "
        "chasing the latest innovation for its own sake, but by carefully evaluating whether a "
        "technology reliably serves people and existing, proven processes before adopting it "
        "broadly. Toyota is known for being deliberately cautious about new technology, often "
        "waiting until a technology has been thoroughly tested and proven stable before rolling "
        "it out widely.",

        "This caution is not technophobia. Toyota invests heavily in technology and automation "
        "where it demonstrably helps flow, quality, or safety. The key test is whether the "
        "technology fits the existing philosophy and supports people rather than replacing "
        "thoughtful human judgment or destabilizing a process that is already working well. "
        "New technology that conflicts with reliability, flow, or standardized work is treated "
        "with skepticism until proven otherwise.",

        "A common failure mode Toyota tries to avoid is adopting new technology that forces "
        "people to change proven, stable processes just to accommodate the tool, rather than "
        "the technology being adapted to support the process. Pilot testing on a small scale, "
        "with cross-functional review of the impact on flow, quality, and people, is the "
        "typical path before any large-scale rollout.",

        "The principle also emphasizes that technology should never be used to replace "
        "the fundamentals such as standardized work, visual control, and problem-solving "
        "culture. Instead, well-chosen technology should make these fundamentals easier and "
        "more effective — for example, sensors that make abnormalities easier to detect "
        "instantly, without removing a worker's ability to understand and act on what is "
        "happening.",
    ],
    "questions": [
        {
            "q": "What is Toyota's general approach to adopting new technology under Principle 8?",
            "options": [
                "Adopt every new technology immediately to stay ahead of competitors",
                "Carefully evaluate and thoroughly test technology before broad adoption",
                "Avoid all new technology permanently",
                "Let each department choose technology without any evaluation"
            ],
            "correct": 1,
            "explanation": "Toyota is deliberately cautious, testing technology thoroughly before rolling it out widely."
        },
        {
            "q": "Does Principle 8 mean Toyota avoids technology and automation altogether?",
            "options": [
                "Yes, Toyota avoids all automation",
                "No, Toyota invests in technology where it demonstrably helps flow, quality, or safety",
                "Yes, only in office settings",
                "No, but only for financial software"
            ],
            "correct": 1,
            "explanation": "Toyota is not against technology; it insists that technology proven to help people and process is worth adopting."
        },
        {
            "q": "What is a common failure mode Toyota tries to avoid regarding new technology?",
            "options": [
                "Adapting technology to fit and support existing proven processes",
                "Forcing people to change stable, proven processes just to accommodate a new tool",
                "Testing technology on a small scale before rollout",
                "Reviewing technology's impact on quality and people"
            ],
            "correct": 1,
            "explanation": "The failure mode is letting technology dictate disruptive process changes rather than fitting the technology to the process."
        },
        {
            "q": "What is the typical path before large-scale technology rollout, according to the material?",
            "options": [
                "Immediate company-wide implementation with no testing",
                "Pilot testing on a small scale with cross-functional review of impact",
                "Skipping evaluation entirely to save time",
                "Outsourcing all technology decisions to vendors"
            ],
            "correct": 1,
            "explanation": "Small-scale pilots with cross-functional review help validate a technology before wide rollout."
        },
        {
            "q": "What should new technology never be used to replace, according to Principle 8?",
            "options": [
                "Standardized work, visual control, and the problem-solving culture",
                "Outdated equipment that is unsafe",
                "Manual paperwork processes",
                "Slow, unreliable machines"
            ],
            "correct": 0,
            "explanation": "Technology should support these fundamentals, not replace or undermine them."
        },
        {
            "q": "What is the key test Toyota applies when considering new technology?",
            "options": [
                "Whether it is the newest option on the market",
                "Whether it reliably serves people and fits existing, proven processes",
                "Whether competitors have already adopted it",
                "Whether it is the cheapest available option"
            ],
            "correct": 1,
            "explanation": "The core test is reliability and fit with people and process, not novelty or cost alone."
        },
        {
            "q": "How should well-chosen technology affect standardized work and visual control?",
            "options": [
                "It should eliminate the need for them entirely",
                "It should make these fundamentals easier and more effective, not replace them",
                "It should conflict with them to force change",
                "It should have no relationship to them"
            ],
            "correct": 1,
            "explanation": "Good technology strengthens fundamentals like visual control rather than substituting for them."
        },
        {
            "q": "Why might Toyota treat a new, unproven technology with skepticism?",
            "options": [
                "Because it might destabilize a process that already works well or conflict with flow and reliability",
                "Because all new technology is inherently bad",
                "Because skepticism guarantees faster adoption",
                "Because technology has no impact on process reliability"
            ],
            "correct": 0,
            "explanation": "Unproven technology risks undermining stable, reliable, already-working processes."
        },
        {
            "q": "Which example illustrates technology 'serving people' rather than replacing judgment?",
            "options": [
                "A sensor that detects abnormalities instantly while still letting workers understand and act on the situation",
                "A fully automated system that removes all human oversight of quality",
                "Software that hides problem data from workers",
                "A tool that forces workers to abandon a proven, stable process"
            ],
            "correct": 0,
            "explanation": "This example shows technology enhancing detection while preserving human understanding and action, consistent with the principle."
        },
        {
            "q": "What is the overarching message of Principle 8?",
            "options": [
                "Technology decisions should be driven by hype and speed of adoption",
                "Technology should be reliable, thoroughly tested, and should serve people and proven processes",
                "New technology should always override existing standards immediately",
                "Automation should replace all human roles as quickly as possible"
            ],
            "correct": 1,
            "explanation": "This is the essence of Principle 8: technology must be reliable, tested, and supportive of people and process."
        }
    ]
})

PRINCIPLES.append({
    "number": 9,
    "section": "Section III: Add Value to the Organization by Developing Your People and Partners",
    "title": "Grow leaders who thoroughly understand the work, live the philosophy, and teach it to others.",
    "content": [
        "Principle 9 rejects the common practice of hiring senior leaders primarily from "
        "outside the organization or from purely academic management backgrounds. Instead, "
        "Toyota strongly prefers to grow leaders from within, people who have done the actual "
        "work on the floor, understand its details intimately, and have internalized the "
        "company's philosophy through years of lived experience rather than a slide deck.",

        "A leader who deeply understands the work can coach effectively, ask the right "
        "questions during problem-solving, and recognize when a proposed solution is "
        "superficial versus addressing a true root cause. Leaders who lack this grounding tend "
        "to rely on generic management techniques that may look good in a presentation but "
        "don't fit the specific realities of the business.",

        "Beyond technical competence, Toyota leaders are expected to be teachers. A core part "
        "of a leader's job is developing the people below them, passing on both technical "
        "know-how and the underlying philosophy — patience, respect for people, relentless "
        "problem-solving — so the culture perpetuates itself across generations of employees "
        "rather than eroding as founders and early leaders retire.",

        "This principle has direct implications for succession planning and promotion "
        "criteria: candidates for leadership are evaluated not just on results, but on how "
        "well they understand the actual work, how effectively they teach and mentor others, "
        "and how consistently they model the organization's principles in daily decisions, "
        "especially under pressure.",
    ],
    "questions": [
        {
            "q": "What does Principle 9 say about how Toyota prefers to develop its senior leaders?",
            "options": [
                "By hiring almost exclusively from outside the company",
                "By growing leaders from within who deeply understand the actual work",
                "By relying only on academic management credentials",
                "By rotating leaders randomly with no relevant experience"
            ],
            "correct": 1,
            "explanation": "Toyota strongly prefers internally grown leaders with hands-on understanding of the work and philosophy."
        },
        {
            "q": "Why does deep understanding of the work matter for effective leadership, according to the material?",
            "options": [
                "It has no effect on coaching or problem-solving ability",
                "It allows leaders to coach effectively and recognize superficial versus root-cause solutions",
                "It only matters for entry-level employees",
                "It replaces the need for any teaching skills"
            ],
              "correct": 1,
            "explanation": "Grounded leaders can ask sharper questions and tell the difference between quick fixes and true root-cause solutions."
        },
        {
            "q": "What key role, beyond technical competence, are Toyota leaders expected to play?",
            "options": [
                "Auditor of financial statements only",
                "Teacher, passing on technical know-how and philosophy to others",
                "External spokesperson exclusively",
                "Sole decision-maker with no delegation"
            ],
            "correct": 1,
            "explanation": "Leaders are expected to actively teach and develop the people around them, sustaining the culture."
        },
        {
            "q": "What risk does the material associate with leaders who lack grounding in the actual work?",
            "options": [
                "They tend to rely on generic management techniques that may not fit the business's realities",
                "They automatically become better teachers",
                "They have no impact on organizational culture",
                "They always outperform internally grown leaders"
            ],
            "correct": 0,
            "explanation": "Without hands-on grounding, leaders may apply generic approaches that miss important specifics of the business."
        },
        {
            "q": "How does Principle 9 influence promotion and succession planning?",
            "options": [
                "Candidates are judged solely on short-term financial results",
                "Candidates are evaluated on understanding of the work, teaching ability, and modeling the philosophy",
                "Promotions are decided entirely at random",
                "Only external hires are considered for leadership roles"
            ],
            "correct": 1,
            "explanation": "Leadership evaluation includes understanding of the work, mentoring effectiveness, and consistent modeling of principles."
        },
        {
            "q": "What philosophical elements are leaders expected to pass on to others, beyond technical skills?",
            "options": [
                "Patience, respect for people, and relentless problem-solving",
                "Only financial targets",
                "Strict avoidance of all delegation",
                "A preference for short-term thinking"
            ],
            "correct": 0,
            "explanation": "Leaders transmit both technical know-how and cultural values like patience, respect, and problem-solving rigor."
        },
        {
            "q": "What is the long-term risk if leaders do not actively teach and develop others?",
            "options": [
                "The culture perpetuates itself automatically with no effort",
                "The culture may erode as founders and early leaders retire",
                "There is no risk; culture is unrelated to leadership behavior",
                "Only technical skills are lost, never cultural values"
            ],
            "correct": 1,
            "explanation": "Without active teaching, the organization's philosophy risks fading as experienced leaders leave."
        },
        {
            "q": "What does it mean for a leader to 'live the philosophy,' as described in Principle 9?",
            "options": [
                "Reciting company values without applying them",
                "Consistently modeling the organization's principles in daily decisions, especially under pressure",
                "Only following the philosophy during public presentations",
                "Ignoring the philosophy when it is inconvenient"
            ],
            "correct": 1,
            "explanation": "Living the philosophy means consistent behavior aligned with principles, particularly when under pressure."
        },
        {
            "q": "Why might a leader hired purely for academic credentials struggle under this principle?",
            "options": [
                "Because academic credentials guarantee deep operational understanding",
                "Because they may lack the hands-on, lived experience needed to coach and judge root causes effectively",
                "Because academic credentials are irrelevant to any organization",
                "Because Toyota never hires anyone with academic backgrounds"
            ],
            "correct": 1,
            "explanation": "The principle emphasizes lived, hands-on experience as essential grounding for effective leadership at Toyota."
        },
        {
            "q": "What is the central idea of Principle 9?",
            "options": [
                "Leaders should be selected without regard to their understanding of the work",
                "Leaders should deeply understand the work, embody the philosophy, and actively teach it to others",
                "Leadership development is unnecessary if results are good",
                "External hires are always preferable to internal promotions"
            ],
            "correct": 1,
            "explanation": "This summarizes Principle 9's core requirement: understanding, living, and teaching the philosophy as a leader."
        }
    ]
})

PRINCIPLES.append({
    "number": 10,
    "section": "Section III: Add Value to the Organization by Developing Your People and Partners",
    "title": "Develop exceptional people and teams who follow your company's philosophy.",
    "content": [
        "While Principle 9 focuses on individual leaders, Principle 10 broadens the lens to the "
        "entire workforce and the teams they form. Toyota invests heavily and continuously in "
        "training, cross-training, and team-based problem-solving skills so that ordinary "
        "employees, working together, can achieve extraordinary and consistent results.",

        "A defining feature of this principle is the emphasis on teamwork over individual "
        "heroics. Toyota structures work around small teams with a team leader who provides "
        "hands-on support, covers for absent members, and actively coaches problem-solving in "
        "real time, rather than isolated individuals who each optimize their own narrow task "
        "without regard for the whole.",

        "Training at Toyota is deliberately hands-on and repetitive, following an approach "
        "similar to the Training Within Industry (TWI) method: show, explain, demonstrate, and "
        "then have the trainee perform the task while being observed and coached, repeated "
        "until the standard is met reliably. This produces genuinely skilled employees rather "
        "than people who have merely watched a video or read a manual once.",

        "Ultimately, this principle asserts that a company's competitive advantage comes from "
        "its people and how well they embody its philosophy and problem-solving culture — not "
        "merely from its equipment, patents, or capital. Investing in people is treated as a "
        "long-term investment in organizational capability, directly connected back to "
        "Principle 1's long-term philosophy.",
    ],
    "questions": [
        {
            "q": "How does Principle 10 differ in focus from Principle 9?",
            "options": [
                "It focuses exclusively on financial metrics",
                "It broadens the focus from individual leaders to the entire workforce and teams",
                "It applies only to executives, not general employees",
                "It has no relationship to Principle 9"
            ],
            "correct": 1,
            "explanation": "Principle 10 extends the development focus from leaders alone to exceptional people and teams throughout the organization."
        },
        {
            "q": "What does Toyota emphasize over individual heroics, according to Principle 10?",
            "options": [
                "Isolated individual achievement",
                "Teamwork, with team leaders providing hands-on support and coaching",
                "Competition between employees for individual recognition",
                "Eliminating teams in favor of solo work"
            ],
            "correct": 1,
            "explanation": "Toyota structures work around teams supported by hands-on team leaders rather than isolated individual effort."
        },
        {
            "q": "What training approach does the material compare Toyota's method to?",
            "options": [
                "Training Within Industry (TWI): show, explain, demonstrate, then observe and coach",
                "One-time video training with no follow-up",
                "Fully self-directed learning with no supervision",
                "Purely theoretical classroom lectures only"
            ],
            "correct": 0,
            "explanation": "The described method mirrors TWI's hands-on, repeated demonstration-and-practice approach."
        },
        {
            "q": "Why is repeated, hands-on training emphasized rather than a single viewing of a manual or video?",
            "options": [
                "Because it produces genuinely skilled employees who reliably meet the standard",
                "Because repetition is discouraged in skill-building",
                "Because manuals and videos are always more effective",
                "Because Toyota avoids all formal training"
            ],
            "correct": 0,
            "explanation": "Repeated practice with observation and coaching builds real competence, unlike passive one-time exposure."
        },
        {
            "q": "According to Principle 10, what is a company's true competitive advantage rooted in?",
            "options": [
                "Its equipment and patents alone",
                "Its people and how well they embody the philosophy and problem-solving culture",
                "Its stock price",
                "Its advertising budget"
            ],
            "correct": 1,
            "explanation": "The principle argues that people and culture, not just capital or equipment, drive lasting competitive advantage."
        },
        {
            "q": "What role does a Toyota team leader typically play within a small team?",
            "options": [
                "Remains uninvolved in daily operations",
                "Provides hands-on support, covers for absences, and coaches real-time problem-solving",
                "Only handles administrative paperwork",
                "Discourages any team collaboration"
            ],
            "correct": 1,
            "explanation": "Team leaders are actively engaged, supporting the team directly rather than managing from a distance."
        },
        {
            "q": "How does investing in people under Principle 10 relate to Principle 1?",
            "options": [
                "It contradicts the long-term philosophy of Principle 1",
                "It reflects the same long-term investment mindset described in Principle 1",
                "The two principles are entirely unrelated",
                "Principle 10 replaces the need for Principle 1"
            ],
            "correct": 1,
            "explanation": "Developing people is framed as a long-term investment in capability, consistent with the long-term philosophy in Principle 1."
        },
        {
            "q": "What does Toyota invest in continuously according to Principle 10?",
            "options": [
                "Only initial onboarding with no follow-up",
                "Training, cross-training, and team-based problem-solving skills",
                "Exclusively executive education programs",
                "Advertising campaigns targeting employees"
            ],
            "correct": 1,
            "explanation": "Continuous investment in training and team skills is central to developing exceptional people and teams."
        },
        {
            "q": "What outcome does Toyota expect from strong team-based structures?",
            "options": [
                "Ordinary employees achieving extraordinary and consistent results together",
                "Only a few star performers succeeding while others are ignored",
                "Reduced overall performance compared to individual work",
                "No measurable impact on results"
            ],
            "correct": 0,
            "explanation": "Well-supported teams of ordinary employees can consistently achieve excellent results through Toyota's approach."
        },
        {
            "q": "What is the central message of Principle 10?",
            "options": [
                "Develop exceptional individuals and teams who embody the company's philosophy",
                "Minimize investment in employee training to cut costs",
                "Rely solely on individual star performers",
                "Treat teamwork as unnecessary for operational success"
            ],
            "correct": 0,
            "explanation": "This captures Principle 10's core focus on developing people and teams aligned with the company's philosophy."
        }
    ]
})

PRINCIPLES.append({
    "number": 11,
    "section": "Section III: Add Value to the Organization by Developing Your People and Partners",
    "title": "Respect your extended network of partners and suppliers by challenging them and helping them improve.",
    "content": [
        "Principle 11 extends Toyota's philosophy of people development beyond its own "
        "employees to its suppliers and business partners. Rather than treating suppliers as "
        "interchangeable vendors to be squeezed on price, Toyota views them as an extension of "
        "its own production system, worthy of the same long-term investment and the same "
        "combination of high standards and genuine support.",

        "This shows up in practice as demanding, rigorous expectations — suppliers are held to "
        "exacting quality and delivery standards, and are challenged to continuously improve "
        "just as internal teams are. But this challenge comes paired with real help: Toyota "
        "sends its own engineers to work alongside struggling suppliers, shares problem-solving "
        "methods and even proprietary techniques, and invests time in building the supplier's "
        "internal capability rather than simply replacing them when problems arise.",

        "This 'partner, don't punish' approach stands in contrast to purely transactional "
        "supplier relationships common elsewhere, where the primary lever is switching vendors "
        "whenever a marginally cheaper option appears. Toyota's long-term supplier "
        "relationships allow for deeper trust, shared investment in tooling and capability, and "
        "a willingness from suppliers to flag problems early rather than hide them for fear of "
        "losing the contract.",

        "The principle applies the same logic used internally — respect for people paired with "
        "high expectations drives improvement — to the entire extended value chain. A supplier "
        "network developed this way becomes a genuine competitive advantage, since capability, "
        "trust, and problem-solving culture extend well beyond the walls of Toyota's own "
        "factories.",
    ],
    "questions": [
        {
            "q": "How does Toyota primarily view its suppliers under Principle 11?",
            "options": [
                "As interchangeable vendors to be replaced whenever a cheaper option appears",
                "As an extension of its own production system worthy of long-term investment",
                "As competitors to be undermined",
                "As irrelevant to overall product quality"
            ],
            "correct": 1,
            "explanation": "Toyota treats suppliers as partners integrated into its broader production system, not disposable vendors."
        },
        {
            "q": "What does 'challenging' suppliers look like in practice, according to the material?",
            "options": [
                "Ignoring supplier performance entirely",
                "Holding suppliers to rigorous quality and delivery standards, expecting continuous improvement",
                "Only challenging suppliers on price, never quality",
                "Avoiding any performance expectations for suppliers"
            ],
            "correct": 1,
            "explanation": "Suppliers are held to demanding standards and pushed to improve, mirroring internal expectations."
        },
        {
            "q": "How does Toyota pair high expectations for suppliers with genuine support?",
            "options": [
                "By sending engineers to work alongside struggling suppliers and sharing problem-solving methods",
                "By cutting off communication when a supplier struggles",
                "By replacing any supplier immediately upon a single mistake",
                "By refusing to share any internal techniques"
            ],
            "correct": 0,
            "explanation": "Toyota actively invests resources and expertise to help suppliers build capability, not just demands performance."
        },
        {
            "q": "What is the described alternative approach that Toyota's supplier philosophy contrasts with?",
            "options": [
                "Long-term, trust-based partnership",
                "Purely transactional relationships focused on switching vendors for marginal price savings",
                "Government-mandated supplier contracts",
                "No supplier relationships at all"
            ],
            "correct": 1,
            "explanation": "Toyota's approach is contrasted with transactional, price-driven vendor switching common elsewhere."
        },
        {
            "q": "What benefit does long-term supplier trust provide, according to the material?",
            "options": [
                "Suppliers hide problems for fear of losing contracts",
                "Suppliers are more willing to flag problems early rather than concealing them",
                "Trust has no effect on problem reporting",
                "Long-term trust always increases costs with no benefit"
            ],
            "correct": 1,
            "explanation": "Deeper trust encourages suppliers to surface problems early rather than hide them out of fear."
        },
        {
            "q": "What phrase captures Toyota's overall supplier philosophy in the material?",
            "options": [
                "'Punish and replace'",
                "'Partner, don't punish'",
                "'Switch whenever cheaper'",
                "'Ignore and outsource'"
            ],
            "correct": 1,
            "explanation": "The material explicitly describes this as a 'partner, don't punish' approach."
        },
        {
            "q": "How does Principle 11 relate to Toyota's internal people-development principles?",
            "options": [
                "It applies the same respect-plus-high-expectations logic to the extended supplier network",
                "It has no connection to internal development principles",
                "It replaces internal development entirely with supplier development",
                "It only applies to Toyota's competitors"
            ],
            "correct": 0,
            "explanation": "The same combination of respect and high expectations used with employees is extended to suppliers and partners."
        },
        {
            "q": "What kind of investment does Toyota make in its supplier relationships, according to the material?",
            "options": [
                "Investment in shared tooling, capability building, and long-term trust",
                "Investment only in legal contracts with no operational involvement",
                "No investment beyond the initial purchase order",
                "Investment exclusively in marketing partnerships"
            ],
            "correct": 0,
            "explanation": "Toyota invests in building supplier capability, shared tooling, and long-term trust, not just transactional contracts."
        },
        {
            "q": "Why does a well-developed supplier network become a competitive advantage for Toyota?",
            "options": [
                "Because it extends capability, trust, and problem-solving culture beyond Toyota's own factories",
                "Because it eliminates the need for quality control",
                "Because it makes suppliers entirely dependent with no independent capability",
                "Because it reduces the number of suppliers to zero"
            ],
            "correct": 0,
            "explanation": "A strong supplier network extends Toyota's operational strengths across its entire value chain."
        },
        {
            "q": "What is the central idea of Principle 11?",
            "options": [
                "Suppliers should be squeezed on price with no support",
                "Respect and help partners and suppliers improve while holding them to high standards",
                "Suppliers are irrelevant to organizational success",
                "Only internal teams matter for continuous improvement"
            ],
            "correct": 1,
            "explanation": "This is the essence of Principle 11: respect combined with challenge and genuine support for the extended partner network."
        }
    ]
})

PRINCIPLES.append({
    "number": 12,
    "section": "Section IV: Continuously Solving Root Problems Drives Organizational Learning",
    "title": "Go and see for yourself to thoroughly understand the situation (Genchi Genbutsu).",
    "content": [
        "Genchi genbutsu translates roughly as 'go and see' or 'actual place, actual thing.' "
        "It is Toyota's insistence that decisions and problem-solving should be grounded in "
        "direct, first-hand observation of where the work actually happens, rather than relying "
        "solely on reports, dashboards, or secondhand summaries produced by someone else.",

        "Reports and data are useful, but they are always an abstraction — filtered, "
        "summarized, and sometimes distorted by the person creating them. A manager who only "
        "reads a report about a quality problem may miss critical context: the awkward angle a "
        "worker has to reach at, the subtle noise a machine makes just before it fails, or the "
        "informal workaround that operators have adopted because the official process doesn't "
        "actually work in practice.",

        "Practicing genchi genbutsu means physically walking to the shop floor, the warehouse, "
        "the customer's site, or wherever the actual work or problem exists, observing "
        "carefully, and often asking direct questions of the people doing the work before "
        "forming conclusions or approving a solution. This is why senior Toyota executives are "
        "expected to regularly spend time on the floor, not just in meeting rooms reviewing "
        "slides.",

        "This principle also shapes how problems are investigated: rather than guessing at a "
        "root cause from a desk, problem-solvers are expected to go to where the defect "
        "occurred, examine the actual part or process, and gather firsthand facts before asking "
        "'why' repeatedly to trace the chain of causation. Decisions made this way tend to be "
        "far more accurate and durable than those made purely from secondhand information.",
    ],
    "questions": [
        {
            "q": "What does genchi genbutsu mean?",
            "options": [
                "'Go and see' — actual place, actual thing",
                "'Trust the report' — rely only on written summaries",
                "'Delegate everything' — avoid direct observation",
                "'Guess the cause' — skip investigation"
            ],
            "correct": 0,
            "explanation": "Genchi genbutsu literally emphasizes going to the actual place to see the actual thing firsthand."
        },
        {
            "q": "Why does the material caution against relying solely on reports and dashboards?",
            "options": [
                "Because reports are always completely accurate",
                "Because reports are abstractions that can be filtered, summarized, or distorted",
                "Because reports are illegal to use at Toyota",
                "Because dashboards replace the need for any decision-making"
            ],
            "correct": 1,
            "explanation": "Reports lose critical context and nuance that direct observation can reveal."
        },
        {
            "q": "What kind of context might a manager miss by only reading a report about a quality problem?",
            "options": [
                "Precise financial totals",
                "Subtle details like an awkward work posture, unusual machine noise, or informal workarounds",
                "The report's publication date",
                "The name of the report's author"
            ],
            "correct": 1,
            "explanation": "First-hand observation reveals subtle, practical details that reports often omit."
        },
        {
            "q": "What are senior Toyota executives expected to do regularly, according to Principle 12?",
            "options": [
                "Stay exclusively in meeting rooms reviewing slides",
                "Spend time on the floor observing actual work directly",
                "Avoid any direct contact with frontline workers",
                "Rely entirely on quarterly written summaries"
            ],
            "correct": 1,
            "explanation": "Genchi genbutsu expects leaders to personally observe where work happens, not just review reports."
        },
        {
            "q": "How does genchi genbutsu shape problem investigation?",
            "options": [
                "Problem-solvers are expected to guess root causes from a desk",
                "Problem-solvers go to where the defect occurred and gather firsthand facts before analysis",
                "Problem-solvers rely only on secondhand accounts from other departments",
                "Problem-solvers skip investigation and act on assumptions"
            ],
            "correct": 1,
            "explanation": "Direct, firsthand fact-gathering at the actual location is central to effective root-cause investigation."
        },
        {
            "q": "What technique is commonly paired with going to the actual place, according to the material?",
            "options": [
                "Asking 'why' repeatedly to trace the chain of causation",
                "Skipping all questioning and accepting the first explanation",
                "Relying solely on statistical averages",
                "Ignoring firsthand facts in favor of assumptions"
            ],
            "correct": 0,
            "explanation": "Genchi genbutsu is often paired with repeated 'why' questioning to trace true root causes."
        },
        {
            "q": "What is one practical way genchi genbutsu is applied outside the factory?",
            "options": [
                "Visiting a customer's site to directly observe how a product is used",
                "Only reading customer surveys, never engaging directly",
                "Delegating all customer understanding to marketing reports",
                "Avoiding any customer contact"
            ],
            "correct": 0,
            "explanation": "Genchi genbutsu extends to understanding customer contexts through direct observation, not just secondhand data."
        },
        {
            "q": "According to the material, why are decisions made through direct observation typically more durable?",
            "options": [
                "Because they are based on firsthand facts rather than filtered secondhand information",
                "Because they take less time than reviewing reports",
                "Because they avoid asking any questions of workers",
                "Because they are always cheaper to implement"
            ],
            "correct": 0,
            "explanation": "Firsthand understanding leads to more accurate and lasting decisions compared to relying on filtered reports."
        },
        {
            "q": "What might a worker's informal workaround reveal that a report would not, according to the material?",
            "options": [
                "That the official process doesn't actually work in practice",
                "That the report is always wrong",
                "That workers never adapt processes",
                "That workarounds are irrelevant to problem-solving"
            ],
            "correct": 0,
            "explanation": "Informal workarounds often signal a mismatch between the official process and real working conditions, visible only through direct observation."
        },
        {
            "q": "What is the central idea of Principle 12?",
            "options": [
                "Base decisions on direct, firsthand observation of the actual situation",
                "Trust secondhand reports over direct observation",
                "Avoid visiting the shop floor whenever possible",
                "Make decisions purely from historical financial data"
            ],
            "correct": 0,
            "explanation": "Genchi genbutsu is fundamentally about grounding decisions in direct, firsthand understanding."
        }
    ]
})

PRINCIPLES.append({
    "number": 13,
    "section": "Section IV: Continuously Solving Root Problems Drives Organizational Learning",
    "title": "Make decisions slowly by consensus, thoroughly considering all options; implement decisions rapidly (Nemawashi).",
    "content": [
        "Nemawashi, literally 'going around the roots,' describes Toyota's deliberate, "
        "consensus-building approach to major decisions. Before a decision is finalized, it is "
        "quietly discussed with all relevant stakeholders individually or in small groups, "
        "gathering input, surfacing objections, and building shared understanding, well before "
        "any formal meeting or announcement.",

        "This may look slow compared to a single decisive executive simply issuing an order, "
        "and in the short run, it is slower. Toyota accepts this deliberately, because a "
        "decision that has been thoroughly vetted from multiple angles and has genuine buy-in "
        "across the people who must execute it tends to avoid costly late-stage surprises, "
        "resistance, or misunderstandings that a rushed top-down decision often creates.",

        "The payoff comes at implementation. Because nemawashi has already surfaced and "
        "resolved disagreements, and because everyone involved understands the reasoning and "
        "has had a genuine chance to shape the decision, execution can move remarkably fast — "
        "there is no need to re-litigate the decision or manage hidden resistance once it is "
        "formally announced. Slow deliberation up front buys fast, smooth execution afterward.",

        "This approach also reflects respect for people: it treats those who will be affected "
        "by or responsible for executing a decision as valuable sources of insight rather than "
        "passive recipients of instructions. It naturally surfaces a wider range of options and "
        "potential problems than a decision made by one person or a small closed group, "
        "improving the quality of the final choice.",
    ],
    "questions": [
        {
            "q": "What does 'nemawashi' literally mean?",
            "options": [
                "'Going around the roots'",
                "'Stop the line immediately'",
                "'Push harder for speed'",
                "'Ignore all objections'"
            ],
            "correct": 0,
            "explanation": "Nemawashi literally translates to 'going around the roots,' describing a careful, foundational consensus-building process."
        },
        {
            "q": "What happens before a major decision is formally finalized under nemawashi?",
            "options": [
                "It is announced immediately with no prior discussion",
                "It is quietly discussed with relevant stakeholders individually or in small groups to gather input",
                "It is decided solely by one executive in isolation",
                "It is delayed indefinitely with no resolution"
            ],
            "correct": 1,
            "explanation": "Nemawashi involves informal consultation with stakeholders before any formal decision announcement."
        },
        {
            "q": "Why does Toyota accept that nemawashi makes the decision-making phase slower?",
            "options": [
                "Because slowness has no benefit and is simply tolerated",
                "Because thorough vetting and genuine buy-in avoid costly late-stage surprises and resistance",
                "Because Toyota prefers all processes to be slow regardless of value",
                "Because faster decisions are always better in every case"
            ],
            "correct": 1,
            "explanation": "The upfront time investment prevents bigger problems and resistance later in execution."
        },
        {
            "q": "What is the payoff of nemawashi during implementation?",
            "options": [
                "Implementation becomes slower and more contentious",
                "Execution can move quickly because disagreements were already surfaced and resolved",
                "There is no effect on implementation speed",
                "Implementation requires re-litigating the decision constantly"
            ],
            "correct": 1,
            "explanation": "Because consensus was built beforehand, execution proceeds quickly without hidden resistance."
        },
        {
            "q": "How does nemawashi reflect 'respect for people'?",
            "options": [
                "By ignoring the input of those affected by a decision",
                "By treating people who will execute or be affected by a decision as valuable sources of insight",
                "By excluding frontline workers from any discussion",
                "By making all decisions in total secrecy"
            ],
            "correct": 1,
            "explanation": "Consulting affected stakeholders shows respect for their knowledge and stake in the outcome."
        },
        {
            "q": "What tends to happen when a decision is made quickly by a single top-down order without consensus-building?",
            "options": [
                "It always executes faster with no downsides",
                "It can create resistance, misunderstandings, or costly surprises during execution",
                "It automatically has full buy-in from everyone",
                "It eliminates the need for any implementation planning"
            ],
            "correct": 1,
            "explanation": "Skipping consensus-building can lead to problems surfacing later, during execution, that slow things down."
        },
        {
            "q": "How does nemawashi improve the quality of the final decision?",
            "options": [
                "By surfacing a wider range of options and potential problems than a small closed group would find",
                "By limiting input strictly to senior executives",
                "By discouraging any dissenting opinions",
                "By finalizing decisions before any consultation occurs"
            ],
            "correct": 0,
            "explanation": "Broad consultation surfaces more perspectives, options, and risks than a narrow decision-making process."
        },
        {
            "q": "What is the overall trade-off described by Principle 13?",
            "options": [
                "Fast decisions followed by fast, chaotic execution",
                "Slow, thorough decision-making followed by fast, smooth execution",
                "Slow decisions followed by slow execution with no benefit",
                "No trade-off exists between decision speed and execution speed"
            ],
            "correct": 1,
            "explanation": "Principle 13 describes deliberately slow decision-making that enables fast, smooth implementation afterward."
        },
        {
            "q": "Who is typically consulted during the nemawashi process?",
            "options": [
                "Only the most senior executive with no other input",
                "All relevant stakeholders who will be affected by or responsible for executing the decision",
                "Only external consultants unfamiliar with the situation",
                "No one; decisions are made in isolation"
            ],
            "correct": 1,
            "explanation": "Nemawashi is inclusive of the people connected to the decision, not just top leadership."
        },
        {
            "q": "What is the central idea of Principle 13?",
            "options": [
                "Make decisions slowly through broad consensus, then implement them rapidly",
                "Make decisions instantly without any consultation",
                "Avoid implementing decisions once they are made",
                "Consensus-building is unnecessary for major decisions"
            ],
            "correct": 0,
            "explanation": "This captures the essence of nemawashi: deliberate, consensus-driven decisions followed by rapid execution."
        }
    ]
})

PRINCIPLES.append({
    "number": 14,
    "section": "Section IV: Continuously Solving Root Problems Drives Organizational Learning",
    "title": "Become a learning organization through relentless reflection (Hansei) and continuous improvement (Kaizen).",
    "content": [
        "The final principle ties the entire Toyota Way together: an organization must "
        "continuously learn from its own experience, both successes and failures, and use that "
        "learning to keep improving indefinitely. This is not a one-time project or an annual "
        "initiative — it is meant to be a permanent, ongoing habit embedded in daily work at "
        "every level of the organization.",

        "Hansei, often translated as 'self-reflection,' is a distinctly Toyota practice of "
        "honestly and often uncomfortably examining what went wrong, even after a project or "
        "milestone that was technically successful. A hansei session does not look for someone "
        "to blame; it looks for the specific, actionable lessons that can prevent the same gap "
        "or mistake from recurring. Without genuine hansei, teams tend to declare victory and "
        "move on, missing valuable learning opportunities hidden inside successes.",

        "Kaizen, meaning 'change for the better' or continuous improvement, is the practical "
        "engine that acts on what hansei reveals. Rather than waiting for occasional large "
        "transformation projects, kaizen encourages frequent, small, incremental improvements "
        "made by the people closest to the work, compounding over time into substantial gains "
        "that a single big initiative could rarely match.",

        "Together, hansei and kaizen create what Toyota calls a learning organization: one "
        "where standardized work (Principle 6) provides a stable baseline, genchi genbutsu "
        "(Principle 12) grounds understanding in reality, nemawashi (Principle 13) builds "
        "aligned decisions, and hansei and kaizen close the loop by turning every experience — "
        "good or bad — into the next incremental improvement. This closes the full circle of "
        "the 14 principles into a self-reinforcing system of continuous organizational "
        "learning.",
    ],
    "questions": [
        {
            "q": "What does 'hansei' mean in the context of Principle 14?",
            "options": [
                "Self-reflection, honestly examining what went wrong even after success",
                "Immediate celebration with no further analysis",
                "Blaming individuals for mistakes",
                "Ignoring past projects entirely"
            ],
            "correct": 0,
            "explanation": "Hansei is a practice of honest self-reflection aimed at extracting lessons, even from successful outcomes."
        },
        {
            "q": "What does 'kaizen' mean?",
            "options": [
                "Change for the better; continuous improvement",
                "A one-time annual transformation project",
                "A financial reporting term",
                "A type of quality inspection tool"
            ],
            "correct": 0,
            "explanation": "Kaizen refers to ongoing, incremental improvement rather than occasional large initiatives."
        },
        {
            "q": "What is the primary purpose of a hansei session?",
            "options": [
                "To assign blame to specific individuals",
                "To find specific, actionable lessons that prevent the same mistake or gap from recurring",
                "To celebrate success without further analysis",
                "To avoid discussing any problems"
            ],
            "correct": 1,
            "explanation": "Hansei focuses on constructive, actionable learning rather than blame or simple celebration."
        },
        {
            "q": "What tends to happen to teams that skip genuine hansei after a successful project?",
            "options": [
                "They automatically improve without effort",
                "They may miss valuable learning opportunities hidden inside the success",
                "They achieve perfect results every time",
                "They eliminate the need for kaizen entirely"
            ],
            "correct": 1,
            "explanation": "Without honest reflection, even successful projects can hide lessons that go unexamined."
        },
        {
            "q": "How does kaizen typically drive improvement, compared to large transformation projects?",
            "options": [
                "Through frequent, small, incremental improvements made by people closest to the work",
                "Through rare, massive overhauls led solely by top executives",
                "Through eliminating all change once a standard is set",
                "Through outsourcing all improvement efforts"
            ],
            "correct": 0,
            "explanation": "Kaizen relies on continuous small improvements from those doing the work, which compound over time."
        },
        {
            "q": "How do standardized work and kaizen relate, based on the material?",
            "options": [
                "Standardized work provides the stable baseline that kaizen then improves upon",
                "Standardized work eliminates any need for kaizen",
                "Kaizen and standardized work are unrelated concepts",
                "Kaizen always precedes the existence of any standard"
            ],
            "correct": 0,
            "explanation": "A stable standard gives kaizen a clear baseline to measure and build improvements from."
        },
        {
            "q": "How does Principle 14 connect to genchi genbutsu (Principle 12) and nemawashi (Principle 13)?",
            "options": [
                "It has no connection to these earlier principles",
                "It closes the loop by turning grounded understanding and aligned decisions into ongoing improvement",
                "It replaces the need for genchi genbutsu and nemawashi",
                "It only applies to financial decisions, unrelated to the earlier principles"
            ],
            "correct": 1,
            "explanation": "Principle 14 integrates the earlier principles into a continuous cycle of learning and improvement."
        },
        {
            "q": "Is hansei meant to be a one-time event according to the material?",
            "options": [
                "Yes, it happens only once at company founding",
                "No, it is meant to be an ongoing, permanent habit at every level of the organization",
                "Yes, it only occurs during annual reviews",
                "No, it is only used by senior executives"
            ],
            "correct": 1,
            "explanation": "Hansei, like kaizen, is meant to be embedded in daily, ongoing organizational practice."
        },
        {
            "q": "What compounding effect does frequent, small-scale kaizen produce over time?",
            "options": [
                "No measurable effect on overall performance",
                "Substantial gains that a single large initiative could rarely match",
                "A decline in overall capability",
                "Immediate, one-time results with no lasting effect"
            ],
            "correct": 1,
            "explanation": "Many small improvements accumulate into significant long-term gains, often exceeding what one large project could achieve."
        },
        {
            "q": "What is the central idea of Principle 14, tying together the full set of 14 principles?",
            "options": [
                "Become a learning organization through relentless reflection and continuous improvement",
                "Focus exclusively on short-term financial wins",
                "Avoid any reflection on past projects",
                "Rely solely on large, infrequent transformation projects"
            ],
            "correct": 0,
            "explanation": "This is the core message of Principle 14, closing the loop on the entire Toyota Way framework."
        }
    ]
})
