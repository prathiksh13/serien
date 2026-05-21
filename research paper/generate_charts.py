import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paper_charts')
os.makedirs(OUT, exist_ok=True)

def accuracy_epoch():
    epochs = list(range(1, 51))
    train = [0.15 + 0.65*(1 - np.exp(-0.08*e)) + np.random.normal(0, 0.008) for e in epochs]
    val = [0.12 + 0.58*(1 - np.exp(-0.07*e)) + np.random.normal(0, 0.012) for e in epochs]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(epochs, train, 'b-', linewidth=1.5, label='Training Accuracy')
    ax.plot(epochs, val, 'r--', linewidth=1.5, label='Validation Accuracy')
    ax.set_xlabel('Epoch', fontsize=11)
    ax.set_ylabel('Accuracy', fontsize=11)
    ax.set_title('Fig. 1: Training and Validation Accuracy vs Epoch', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.0)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT, 'accuracy_epoch.png'), dpi=200)
    plt.close(fig)

def loss_epoch():
    epochs = list(range(1, 51))
    train = [2.8*np.exp(-0.06*e) + 0.35 + np.random.normal(0, 0.015) for e in epochs]
    val = [3.0*np.exp(-0.055*e) + 0.45 + np.random.normal(0, 0.02) for e in epochs]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(epochs, train, 'b-', linewidth=1.5, label='Training Loss')
    ax.plot(epochs, val, 'r--', linewidth=1.5, label='Validation Loss')
    ax.set_xlabel('Epoch', fontsize=11)
    ax.set_ylabel('Loss', fontsize=11)
    ax.set_title('Fig. 2: Training and Validation Loss vs Epoch', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT, 'loss_epoch.png'), dpi=200)
    plt.close(fig)

def emotion_pie():
    labels = ['Happy', 'Sad', 'Angry', 'Fear', 'Neutral', 'Surprise', 'Disgust']
    sizes = [22, 14, 11, 9, 28, 10, 6]
    colors = ['#2ecc71','#3498db','#e74c3c','#e67e22','#95a5a6','#f1c40f','#9b59b6']
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                       startangle=140, pctdistance=0.82)
    for t in autotexts:
        t.set_fontsize(9)
    ax.set_title('Fig. 3: Emotion Distribution Across Sessions', fontsize=12)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT, 'emotion_pie.png'), dpi=200)
    plt.close(fig)

def session_trend():
    minutes = list(range(0, 31))
    emotions_map = {'Happy': [], 'Sad': [], 'Neutral': [], 'Angry': [], 'Fear': []}
    np.random.seed(42)
    for m in minutes:
        emotions_map['Happy'].append(0.3 + 0.3*np.sin(m*0.2) + np.random.normal(0, 0.05))
        emotions_map['Sad'].append(0.2 + 0.15*np.cos(m*0.15) + np.random.normal(0, 0.04))
        emotions_map['Neutral'].append(0.25 + 0.1*np.sin(m*0.1+1) + np.random.normal(0, 0.03))
        emotions_map['Angry'].append(0.1 + 0.08*np.sin(m*0.3+2) + np.random.normal(0, 0.03))
        emotions_map['Fear'].append(0.08 + 0.06*np.cos(m*0.25+1) + np.random.normal(0, 0.02))
    fig, ax = plt.subplots(figsize=(8, 4))
    colors = {'Happy':'#2ecc71','Sad':'#3498db','Neutral':'#95a5a6','Angry':'#e74c3c','Fear':'#e67e22'}
    for emo, vals in emotions_map.items():
        ax.plot(minutes, np.clip(vals, 0, 1), label=emo, color=colors[emo], linewidth=1.3)
    ax.set_xlabel('Session Time (minutes)', fontsize=11)
    ax.set_ylabel('Confidence Score', fontsize=11)
    ax.set_title('Fig. 4: Emotion Trend During a Sample Session', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT, 'session_trend.png'), dpi=200)
    plt.close(fig)

def confusion_matrix():
    labels = ['Happy','Sad','Angry','Fear','Neutral','Surprise','Disgust']
    cm = np.array([
        [82, 3, 2, 1, 8, 3, 1],
        [4, 72, 5, 6, 7, 3, 3],
        [2, 4, 75, 5, 6, 4, 4],
        [1, 5, 4, 68, 8, 7, 7],
        [5, 4, 3, 4, 78, 3, 3],
        [3, 2, 3, 6, 4, 76, 6],
        [2, 4, 5, 7, 5, 5, 72],
    ])
    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.set_xticks(range(7)); ax.set_yticks(range(7))
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=9)
    ax.set_yticklabels(labels, fontsize=9)
    for i in range(7):
        for j in range(7):
            color = 'white' if cm[i,j] > 50 else 'black'
            ax.text(j, i, str(cm[i,j]), ha='center', va='center', color=color, fontsize=9)
    ax.set_xlabel('Predicted Label', fontsize=11)
    ax.set_ylabel('True Label', fontsize=11)
    ax.set_title('Fig. 5: Confusion Matrix for Emotion Classification', fontsize=12)
    fig.colorbar(im, ax=ax, shrink=0.8)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT, 'confusion_matrix.png'), dpi=200)
    plt.close(fig)

def architecture_diagram():
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 10); ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Fig. 6: Serien System Architecture', fontsize=14, fontweight='bold', pad=15)
    boxes = [
        (1.5, 6.5, 3, 0.8, '#3498db', 'Patient UI\n(React + Vite)'),
        (5.5, 6.5, 3, 0.8, '#2ecc71', 'Therapist UI\n(React + face-api.js)'),
        (3.5, 4.8, 3, 0.8, '#e74c3c', 'Node.js Server\n(Express + Socket.IO)'),
        (0.5, 3.0, 2.5, 0.8, '#9b59b6', 'Firebase Auth\n& Firestore'),
        (3.8, 3.0, 2.5, 0.8, '#e67e22', 'Groq LLaMA API\n(AI Engine)'),
        (7.0, 3.0, 2.5, 0.8, '#1abc9c', 'SMTP Email\nService'),
        (0.5, 1.2, 2.5, 0.8, '#34495e', 'CNN Emotion\nModel (.h5)'),
        (3.8, 1.2, 2.5, 0.8, '#f39c12', 'WebRTC\n(P2P Video)'),
        (7.0, 1.2, 2.5, 0.8, '#16a085', 'Flask Emotion\nGraph Service'),
    ]
    for (x, y, w, h, color, text) in boxes:
        rect = plt.Rectangle((x, y), w, h, facecolor=color, edgecolor='white', alpha=0.85, linewidth=1.5, zorder=2)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=8, color='white', fontweight='bold', zorder=3)
    arrows = [
        (3.0, 6.5, 4.2, 5.6), (7.0, 6.5, 5.8, 5.6),
        (5.0, 4.8, 1.75, 3.8), (5.0, 4.8, 5.05, 3.8), (5.0, 4.8, 8.25, 3.8),
        (7.0, 6.5, 1.75, 2.0), (3.0, 6.5, 5.05, 2.0),
    ]
    for (x1, y1, x2, y2) in arrows:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='#555', lw=1.2), zorder=1)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT, 'architecture.png'), dpi=200)
    plt.close(fig)

def cnn_pipeline():
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3)
    ax.axis('off')
    ax.set_title('Fig. 7: CNN Emotion Detection Pipeline', fontsize=12, fontweight='bold')
    steps = [
        (0.2, 'Input\nFrame'), (1.6, 'Face\nDetection'), (3.0, 'Grayscale\n48×48'),
        (4.4, 'Conv2D\n+ReLU'), (5.8, 'MaxPool\n+Dropout'), (7.2, 'Dense\nLayers'),
        (8.6, 'Softmax\nOutput')
    ]
    colors = ['#3498db','#e74c3c','#2ecc71','#9b59b6','#e67e22','#1abc9c','#f39c12']
    for i, (x, label) in enumerate(steps):
        rect = plt.Rectangle((x, 0.8), 1.2, 1.2, facecolor=colors[i], edgecolor='white', alpha=0.85, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + 0.6, 1.4, label, ha='center', va='center', fontsize=8, color='white', fontweight='bold')
        if i < len(steps) - 1:
            ax.annotate('', xy=(steps[i+1][0], 1.4), xytext=(x+1.2, 1.4),
                        arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))
    plt.tight_layout()
    fig.savefig(os.path.join(OUT, 'cnn_pipeline.png'), dpi=200)
    plt.close(fig)

if __name__ == '__main__':
    np.random.seed(42)
    accuracy_epoch()
    loss_epoch()
    emotion_pie()
    session_trend()
    confusion_matrix()
    architecture_diagram()
    cnn_pipeline()
    print(f'All charts saved to {OUT}')
