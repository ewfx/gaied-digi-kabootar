graph LR
    A[Email Inbox] --> B(Email Processing Server);
    B --> C{Text Preprocessing};
    C --> D[Cleaned Text];
    C --> E[Feature Vectors];
    D --> E;
    E --> F[Machine Learning Classifier];
    F --> G[Categorized Email];
    G --> H[Loan System Actions];

    subgraph "Email Processing Server"
      B; C; D; E; F;
    end

    subgraph "Loan Servicing System"
      H;
    end

    style A fill:#lightblue,stroke:#333,stroke-width:2px
    style B fill:#lightyellow,stroke:#333,stroke-width:2px
    style C fill:#lightgreen,stroke:#333,stroke-width:2px
    style F fill:#lightcoral,stroke:#333,stroke-width:2px
    style H fill:#lightcyan,stroke:#333,stroke-width:2px

    %% Pictorial Elements
    linkStyle 0,1,2,3,4,5,6 stroke-width:2px;

    %% Email Icon
    A -->|Incoming Emails| B;

    %% Gear Icon (Preprocessing)
    C -->|Cleaning & Feature Extraction| E;

    %% Brain Icon (ML Classifier)
    F -->|Categorization| G;

    %% Database Icon (Loan System)
    H -->|Actions (e.g. routing, reply)| I[Loan Database];

    %% Text Document Icon (Cleaned text)
    D -->|Cleaned Text| E;

    %% Vector icon (Feature Vectors)
    E -->|Numerical Data| F;

    %% Tag Icon (Categorized Email)
    G -->|Categorized Email| H;

    %% Cloud Icon (Email Inbox)
    style A fill:white,stroke:#333,stroke-width:2px,shape:cloud;
    %% Server Icon (Processing Server)
    style B fill:white,stroke:#333,stroke-width:2px,shape:cylinder;
    %% Cog Icon (Preprocessing)
    style C fill:white,stroke:#333,stroke-width:2px,shape:gear;
    %% Document Icon (Cleaned Text)
    style D fill:white,stroke:#333,stroke-width:2px,shape:rect;
    %% Vector Icon (Feature Vectors)
    style E fill:white,stroke:#333,stroke-width:2px,shape:rect;
    %% Brain Icon (ML Classifier)
    style F fill:white,stroke:#333,stroke-width:2px,shape:ellipse;
    %% Tag Icon (Categorized Email)
    style G fill:white,stroke:#333,stroke-width:2px,shape:tag;
    %% Database Icon
    style I fill:white,stroke:#333,stroke-width:2px,shape:database;
