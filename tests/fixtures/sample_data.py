"""Sample test data and fixtures for scholar.py tests."""

# Sample Google Scholar HTML response for testing parsing
SAMPLE_SCHOLAR_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Google Scholar</title>
</head>
<body>
    <div id="gs_res_ccl_mid">
        <div class="gs_r gs_or gs_scl">
            <div class="gs_ggs gs_fl">
                <div class="gs_ttss">
                    <a href="http://example.com/paper.pdf" target="_blank">[PDF]</a>
                </div>
            </div>
            <div class="gs_ri">
                <h3 class="gs_rt">
                    <a href="http://example.com/paper.html">
                        A Revolutionary Approach to Machine Learning
                    </a>
                </h3>
                <div class="gs_a">
                    JA Smith, AB Jones, CD Williams -
                    <em>Journal of Advanced Computing</em>, 2023 - publisher.com
                </div>
                <div class="gs_rs">
                    This paper presents a groundbreaking methodology for machine learning
                    that significantly improves accuracy while reducing computational overhead...
                </div>
                <div class="gs_fl">
                    <a href="/scholar?cites=1234567890123456789&as_sdt=2005&sciodt=0,5&hl=en">
                        Cited by 42
                    </a>
                    <a href="/scholar?cluster=9876543210987654321&hl=en&as_sdt=0,5">
                        All 5 versions
                    </a>
                    <a href="/scholar?q=related:abcdef1234567890:scholar.google.com/&scioq=machine+learning&hl=en&as_sdt=0,5">
                        Related articles
                    </a>
                </div>
            </div>
        </div>

        <div class="gs_r gs_or gs_scl">
            <div class="gs_ri">
                <h3 class="gs_rt">
                    <a href="http://example2.com/another-paper">
                        Deep Learning Applications in Computer Vision
                    </a>
                </h3>
                <div class="gs_a">
                    XY Zhang, LM Chen - <em>AI Conference Proceedings</em>, 2022 - ieee.org
                </div>
                <div class="gs_rs">
                    A comprehensive survey of deep learning techniques applied to
                    computer vision problems including object detection and recognition...
                </div>
                <div class="gs_fl">
                    <a href="/scholar?cites=2345678901234567890&as_sdt=2005&sciodt=0,5&hl=en">
                        Cited by 156
                    </a>
                    <a href="/scholar?cluster=8765432109876543210&hl=en&as_sdt=0,5">
                        All 12 versions
                    </a>
                </div>
            </div>
        </div>
    </div>

    <div id="gs_res_bdy">
        <div class="gs_ab_mdw">
            About 15,400 results
        </div>
    </div>
</body>
</html>
"""

# Sample BibTeX response
SAMPLE_BIBTEX = """
@article{smith2023revolutionary,
  title={A Revolutionary Approach to Machine Learning},
  author={Smith, John A and Jones, Alice B and Williams, Charlie D},
  journal={Journal of Advanced Computing},
  volume={45},
  number={3},
  pages={123--145},
  year={2023},
  publisher={Advanced Computing Publications}
}
"""

# Sample EndNote response
SAMPLE_ENDNOTE = """
%0 Journal Article
%T A Revolutionary Approach to Machine Learning
%A Smith, John A
%A Jones, Alice B
%A Williams, Charlie D
%J Journal of Advanced Computing
%V 45
%N 3
%P 123-145
%D 2023
%I Advanced Computing Publications
"""

# Mock HTTP responses for different scenarios
MOCK_RESPONSES = {
    "search_results": SAMPLE_SCHOLAR_HTML,
    "bibtex": SAMPLE_BIBTEX,
    "endnote": SAMPLE_ENDNOTE,
    "empty_results": '<html><body><div id="gs_res_ccl_mid"></div></body></html>',
    "error_page": "<html><body><h1>Error 503: Service Unavailable</h1></body></html>",
}
