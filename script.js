const sliderContainer = document.getElementById('slider');
const indicatorsContainer = document.getElementById('indicators');
const childSlideContainer = document.getElementById('child-slide');
const childSlideContent = document.getElementById('child-slide-content');
const closeChildBtn = document.getElementById('closeChildBtn');
let currentSlideIndex = parseInt(localStorage.getItem('cses_presentation_slide')) || 0;
let isChildSlideOpen = false;
let slideData = [];

async function loadData() {
    try {
        const indexRes = await fetch('data/index.json');
        if (!indexRes.ok) throw new Error("Could not load index.json");
        const categories = await indexRes.json();
        
        for (const catFolder of categories) {
            const catRes = await fetch(`data/${catFolder}/category.json`);
            if (!catRes.ok) continue;
            const catData = await catRes.json();
            
            const loadedProblems = [];
            for (const probFile of catData.problems || []) {
                const probRes = await fetch(`data/${catFolder}/${probFile}`);
                if (probRes.ok) {
                    const probData = await probRes.json();
                    loadedProblems.push(probData);
                }
            }
            
            catData.problems = loadedProblems;
            slideData.push(catData);
        }
        
        init();
    } catch (e) {
        console.error("Error loading data:", e);
        sliderContainer.innerHTML = `
            <div style="color:#ef4444; text-align:center; padding: 2rem; background: rgba(0,0,0,0.5); border-radius: 12px; z-index: 1000;">
                <h2 style="margin-bottom: 1rem;">⚠️ Lỗi tải dữ liệu</h2>
                <p>Trình duyệt đã chặn việc đọc file cục bộ do chính sách bảo mật (CORS).</p>
                <p style="margin-top: 0.5rem; color: #cbd5e1;">Hãy chạy file <strong>run.sh</strong> (bằng lệnh <code>bash run.sh</code>) hoặc chạy lệnh <code>python3 -m http.server 8000</code> rồi mở <a href="http://localhost:8000" style="color:#3b82f6;">http://localhost:8000</a> trên trình duyệt.</p>
            </div>
        `;
    }
}

function init() {
    slideData.forEach((data, index) => {
        // Create slide
        const slide = document.createElement('div');
        slide.className = `slide ${index === 0 ? 'active' : 'next'}`;
        
        let problemsHtml = '';
        if (data.problems && data.problems.length > 0) {
            problemsHtml = '<div class="slide-right"><h3>Practice Problems</h3>';
            data.problems.forEach((prob, pIdx) => {
                problemsHtml += `
                    <div class="problem-card" onclick="openChildSlide(${index}, ${pIdx})">
                        <div class="problem-title">${prob.title}</div>
                        <div class="problem-source">${prob.source}</div>
                    </div>
                `;
            });
            problemsHtml += '</div>';
        } else {
            problemsHtml = '<div class="slide-right"><div style="color: #64748b; font-style: italic; padding: 1rem;">Problems coming soon...</div></div>';
        }

        slide.innerHTML = `
            <div class="slide-left">
                <h1 class="slide-title">${data.title}</h1>
                ${data.subtitle ? `<div style="font-size: 1.5rem; color: #94a3b8; margin-top: 0.5rem; font-weight: 400;">${data.subtitle}</div>` : ''}
                <div class="slide-content">${data.content}</div>
            </div>
            ${problemsHtml}
        `;
        sliderContainer.appendChild(slide);

        // Create indicator dot
        const dot = document.createElement('div');
        dot.className = `dot ${index === 0 ? 'active' : ''}`;
        dot.addEventListener('click', () => goToSlide(index));
        indicatorsContainer.appendChild(dot);
    });

    // Keyboard hint
    const hint = document.createElement('div');
    hint.className = 'keyboard-hint';
    hint.innerHTML = 'Use <span class="key">←</span> <span class="key">→</span> keys to navigate';
    document.body.appendChild(hint);
    
    // Ensure index is valid
    if (currentSlideIndex >= slideData.length) {
        currentSlideIndex = 0;
    }
    
    // Set initial slide active state
    updateSlides();
}

function updateSlides() {
    if (slideData.length === 0) return;
    
    // Save to localStorage
    localStorage.setItem('cses_presentation_slide', currentSlideIndex);

    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');

    slides.forEach((slide, index) => {
        slide.className = 'slide'; // Reset class
        if (index === currentSlideIndex) {
            slide.classList.add('active');
        } else if (index < currentSlideIndex) {
            slide.classList.add('prev');
        } else {
            slide.classList.add('next');
        }
    });

    dots.forEach((dot, index) => {
        if (index === currentSlideIndex) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
}

function nextSlide() {
    if (currentSlideIndex < slideData.length - 1) {
        currentSlideIndex++;
        updateSlides();
    }
}

function prevSlide() {
    if (currentSlideIndex > 0) {
        currentSlideIndex--;
        updateSlides();
    }
}

function goToSlide(index) {
    if (index >= 0 && index < slideData.length) {
        currentSlideIndex = index;
        updateSlides();
    }
}

// Event Listeners
document.getElementById('nextBtn').addEventListener('click', nextSlide);
document.getElementById('prevBtn').addEventListener('click', prevSlide);

document.addEventListener('keydown', (e) => {
    if (isChildSlideOpen) {
        if (e.key === 'Escape') {
            closeChildBtn.click();
        }
        return;
    }
    if (e.key === 'ArrowRight') {
        nextSlide();
    } else if (e.key === 'ArrowLeft') {
        prevSlide();
    }
});

window.openChildSlide = function(slideIdx, probIdx) {
    const prob = slideData[slideIdx].problems[probIdx];
    const sampleCode = prob.sampleCode || "// Insert your code into the corresponding JSON file...";
    
    let sourceHtml = prob.source;
    const csesMatch = prob.source.match(/CSES\s+(\d+)/);
    if (csesMatch) {
        sourceHtml = `<a href="https://cses.fi/problemset/task/${csesMatch[1]}" target="_blank" style="color: #60a5fa; text-decoration: underline; text-underline-offset: 4px;">${prob.source} ↗</a>`;
    }
    
    childSlideContent.innerHTML = `
        <div class="cses-problem">
            <h2>${prob.title}</h2>
            <p style="color: #94a3b8; font-size: 1rem;"><strong>Source:</strong> ${sourceHtml}</p>
            <div style="margin-top: 2rem;">
                <p>${prob.statement.replace(/\n/g, '<br>')}</p>
            </div>
            <h3>Input</h3>
            <p>${prob.inputFormat.replace(/\n/g, '<br>')}</p>
            <h3>Output</h3>
            <p>${prob.outputFormat.replace(/\n/g, '<br>')}</p>
            ${prob.constraints ? `<h3>Constraints</h3><div style="margin-bottom: 1rem;">${prob.constraints}</div>` : ''}
            <div style="display: flex; gap: 2rem; margin-top: 2.5rem;">
                <div style="flex: 1;">
                    <h3 style="margin-top: 0; font-size: 1.25rem;">Example Input</h3>
                    <pre>${prob.exampleInput}</pre>
                </div>
                <div style="flex: 1;">
                    <h3 style="margin-top: 0; font-size: 1.25rem;">Example Output</h3>
                    <pre>${prob.exampleOutput}</pre>
                </div>
            </div>
            
            <div style="margin-top: 3rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem; padding-bottom: 2rem;">
                <button id="toggleCodeBtn" class="toggle-code-btn">
                    <span>Code</span>
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 18px; height: 18px; margin-left: 8px;"><polyline points="6 9 12 15 18 9"></polyline></svg>
                </button>
                <div id="sampleCodeBlock" style="display: none; margin-top: 1.5rem;">
                    <pre><code style="color: #86efac; font-family: monospace;">${sampleCode.replace(/</g, '&lt;').replace(/>/g, '&gt;')}</code></pre>
                </div>
            </div>
        </div>
    `;
    
    const toggleCodeBtn = document.getElementById('toggleCodeBtn');
    const sampleCodeBlock = document.getElementById('sampleCodeBlock');
    toggleCodeBtn.addEventListener('click', () => {
        if (sampleCodeBlock.style.display === 'none') {
            sampleCodeBlock.style.display = 'block';
            toggleCodeBtn.querySelector('span').innerText = 'Hide Code';
            toggleCodeBtn.querySelector('svg polyline').setAttribute('points', '18 15 12 9 6 15');
        } else {
            sampleCodeBlock.style.display = 'none';
            toggleCodeBtn.querySelector('span').innerText = 'Code';
            toggleCodeBtn.querySelector('svg polyline').setAttribute('points', '6 9 12 15 18 9');
        }
    });

    childSlideContainer.classList.add('active');
    isChildSlideOpen = true;
    
    // Trigger MathJax rendering if it's available
    if (window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise([childSlideContent]).catch((err) => console.log(err.message));
    }
};

closeChildBtn.addEventListener('click', () => {
    childSlideContainer.classList.remove('active');
    isChildSlideOpen = false;
});

// Start loading data
loadData();
