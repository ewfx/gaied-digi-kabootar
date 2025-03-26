```mermaid
graph TD
    %% Sections and Flow
    
    A[📩 Email Inbox] -->|Incoming Emails 📬| B[🖥️ Email Processing Server];
    B -->|Process & Extract Data| C[⚙️ Text Preprocessing];
    
    C -->|Cleaned Content ✍️| D[📄 Cleaned Text];
    C -->|Extract Features 📊| E[🔢 Feature Vectors];
    D --> E;
    
    E -->|Convert to Numerical Data 🔠| F[🧠 ML Classifier];
    F -->|Classify Email 🏷️| G[🏷️ Categorized Email];
    
    G -->|Forward to Service System 📬| H[💾 Service Request Actions];
    H -->|Store & Process 💾| I[📂 Service Request Database];

    %% Subsections for Clarity
    subgraph "📡 Email Processing Server"
      B;
      C;
      D;
      E;
      F;
    end

    subgraph "🛠️ Service Request System"
      H;
      I;
    end

    %% Style Formatting for Better Readability
    style A fill:#A7C7E7,stroke:#2C3E50,stroke-width:2px
    style B fill:#F9E79F,stroke:#2C3E50,stroke-width:2px
    style C fill:#82E0AA,stroke:#2C3E50,stroke-width:2px
    style D fill:#AED6F1,stroke:#2C3E50,stroke-width:2px
    style E fill:#D7BDE2,stroke:#2C3E50,stroke-width:2px
    style F fill:#F5B7B1,stroke:#2C3E50,stroke-width:2px
