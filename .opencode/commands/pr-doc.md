---
description: Generate robust GitHub PR documentation
agent: build
---

Generate a complete and professional GitHub pull request documentation in Markdown.

Requirements:
- Do not include Jira ticket association.
- Do not include a testing section.
- Include executive summary.
- Include objective and scope.
- Include a table of modified files.
- For each file specify:
  - file path
  - whether it was created, modified, deleted, or renamed
  - what was changed in that file
- Describe each functionality or change in depth.
- If there is a new script, ETL, integration, batch process, or relevant flow, include a Mermaid flow diagram.
- Include resources used: tables, datasets, endpoints, documents, configs, etc.
- Include input and output contracts.
- Include success and failure examples.
- Include risks, considerations, and pending items if applicable.

Expected structure:
1. Executive summary
2. Objective
3. Scope
4. Modified files table
5. Detailed change description
6. Functional/technical flow
7. Mermaid diagram if applicable
8. Data/tables/docs used
9. Input/Output
10. Example success and failure cases
11. Business rules
12. Risks/considerations
13. Pending items
14. References/evidence

Use the current project context and changed files to infer the documentation.
If information is missing, explicitly state assumptions.
