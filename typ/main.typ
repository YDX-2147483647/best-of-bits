#import "@preview/tcdm:0.0.3": load, md
#let (configuration, statistics, assets, body) = load(
  projects-data: json("/build/latest.json"),
  projects-yaml: yaml("/projects.yaml"),
)

#set text(lang: "zh", region: "CN")
#set document(
  title: "best-of-BITs (bytes)",
  description: [
    🏆 北京理工大学相关的精选列表。（又名 bytes）
    A ranked list of awesome BITs — projects related to Beijing Institute of Technology. (aka. bytes)
  ],
  author: "YDX-2147483647",
  keywords: ("beijing-institute-of-technology", "best-of", "tooling"),
)
#assets

#show: html.main

#md.render(
  md.preprocess(read("/" + configuration.markdown_header_file), ..statistics),
  ..md.config,
)

#body

#md.render(
  md.preprocess(read("/" + configuration.markdown_footer_file).replace("[!NOTE]", "**Note**"), ..statistics),
  ..md.config,
)
