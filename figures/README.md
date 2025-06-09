# Figures Directory

This directory contains all figures used in the paper.

## Figure List
1. `framework_architecture.pdf` - Framework architecture diagram
2. `performance_comparison.pdf` - Performance comparison charts
3. `case_study_results.pdf` - Case study results visualization

## Figure Requirements
- All figures should be in PDF format
- Resolution: 300 DPI minimum
- Color space: RGB
- Font: Times New Roman or Arial
- Line weight: 1pt minimum

## Figure Captions
Each figure should have:
- Clear, descriptive caption
- Proper labeling
- Consistent formatting
- Reference in main text

## Usage
Figures are referenced in the main.tex file using:
```latex
\begin{figure}[t]
    \centering
    \includegraphics[width=\columnwidth]{figures/figure_name}
    \caption{Figure caption}
    \label{fig:label}
\end{figure}
```

## Maintenance
- Keep original source files
- Document any modifications
- Update captions as needed
- Maintain version control 