from fastagent import FastAgent, Task, Tool
import json
from typing import Dict, List, Any

class SpecificationPhaseAgent(FastAgent):
    """
    A Fast-agent for handling the Specification Phase of the SPARC framework.
    This agent is responsible for defining project objectives, gathering requirements,
    analyzing user scenarios, and establishing UI/UX guidelines.
    """
    
    def __init__(self, model="claude-sonnet"):
        super().__init__(model=model)
        self.name = "Project Specification Agent"
        self.description = "An agent specialized in project specification, requirements gathering, user scenario analysis, and UI/UX guideline establishment"
        
        # Register tools for the agent
        self.register_tool("document_analysis", self.document_analysis)
        self.register_tool("stakeholder_interview_simulator", self.stakeholder_interview_simulator)
        self.register_tool("user_research_toolkit", self.user_research_toolkit)
        self.register_tool("design_system_analyzer", self.design_system_analyzer)
        self.register_tool("requirements_management_tool", self.requirements_management_tool)
        self.register_tool("specification_generator", self.specification_generator)
        
    def document_analysis(self, document: str) -> Dict[str, Any]:
        """
        Analyze a project document to extract key information
        """
        # Implementation would analyze the document and extract key elements
        # For this example, we'll simulate the analysis
        
        # Using Claude Sonnet to analyze the document
        analysis_prompt = f"""
        Analyze the following project document and extract:
        1. Key objectives mentioned
        2. Functional requirements
        3. Non-functional requirements
        4. Target users or personas
        5. Business context and constraints
        
        Document: {document}
        """
        
        # Simulate calling Claude Sonnet model
        result = {
            "key_objectives": ["Objective 1", "Objective 2"],
            "functional_requirements": ["Requirement 1", "Requirement 2"],
            "non_functional_requirements": ["Performance requirement", "Security requirement"],
            "target_personas": ["Persona 1", "Persona 2"],
            "business_context": ["Constraint 1", "Constraint 2"]
        }
        
        return result
    
    def stakeholder_interview_simulator(self, stakeholders: List[str], context: str) -> Dict[str, Any]:
        """
        Simulate stakeholder interviews to gather requirements and feedback
        """
        # Simulate conducting interviews with stakeholders
        interview_results = {}
        for stakeholder in stakeholders:
            # Using Claude Sonnet to simulate stakeholder perspective
            interview_prompt = f"""
            From the perspective of a {stakeholder} stakeholder, provide input on:
            1. Primary concerns about the project
            2. Key requirements they need fulfilled
            3. Success criteria from their perspective
            4. Potential risks or obstacles
            
            Project context: {context}
            """
            
            # Simulate Claude Sonnet response
            interview_results[stakeholder] = {
                "concerns": ["Concern 1", "Concern 2"],
                "requirements": ["Requirement 1", "Requirement 2"],
                "success_criteria": ["Success metric 1", "Success metric 2"],
                "risks": ["Risk 1", "Risk 2"]
            }
        
        return interview_results
    
    def user_research_toolkit(self, project_context: str) -> Dict[str, Any]:
        """
        Generate user personas and scenarios based on project context
        """
        # Using Claude Sonnet to develop user personas
        persona_prompt = f"""
        Based on the following project context, develop 3 user personas:
        1. Name and basic demographic information
        2. Goals and motivations
        3. Pain points and challenges
        4. Usage patterns and preferences
        5. Technology proficiency
        
        Project context: {project_context}
        """
        
        # Simulate Claude Sonnet generating personas
        personas = [
            {
                "name": "Persona 1",
                "demographics": "Demographic info",
                "goals": ["Goal 1", "Goal 2"],
                "pain_points": ["Pain point 1", "Pain point 2"],
                "usage_patterns": ["Pattern 1", "Pattern 2"],
                "tech_proficiency": "Level of proficiency"
            },
            {
                "name": "Persona 2",
                "demographics": "Demographic info",
                "goals": ["Goal 1", "Goal 2"],
                "pain_points": ["Pain point 1", "Pain point 2"],
                "usage_patterns": ["Pattern 1", "Pattern 2"],
                "tech_proficiency": "Level of proficiency"
            }
        ]
        
        # Generate user journeys
        journeys = [
            {
                "persona": "Persona 1",
                "journey": ["Step 1", "Step 2", "Step 3"],
                "touchpoints": ["Touchpoint 1", "Touchpoint 2"],
                "pain_points": ["Journey pain point 1"]
            }
        ]
        
        return {
            "personas": personas,
            "user_journeys": journeys
        }
    
    def design_system_analyzer(self, project_requirements: str) -> Dict[str, Any]:
        """
        Analyze design systems and establish UI/UX guidelines
        """
        # Using Claude Sonnet to suggest design principles
        design_prompt = f"""
        Based on the following project requirements, suggest:
        1. 5 core design principles
        2. Accessibility standards to follow
        3. UI components that would be appropriate
        4. Visual identity elements (colors, typography, etc.)
        
        Project requirements: {project_requirements}
        """
        
        # Simulate Claude Sonnet response
        design_guidelines = {
            "design_principles": [
                "Principle 1",
                "Principle 2", 
                "Principle 3",
                "Principle 4",
                "Principle 5"
            ],
            "accessibility_standards": [
                "WCAG 2.1 level AA compliance",
                "Screen reader compatibility",
                "Keyboard navigation support"
            ],
            "ui_components": [
                "Component 1",
                "Component 2",
                "Component 3"
            ],
            "visual_identity": {
                "colors": ["Primary color", "Secondary color"],
                "typography": "Typography system",
                "iconography": "Icon system"
            }
        }
        
        return design_guidelines
    
    def requirements_management_tool(self, requirements: List[str]) -> Dict[str, Any]:
        """
        Organize and prioritize requirements
        """
        # Using Claude Sonnet to categorize and prioritize requirements
        prioritization_prompt = f"""
        Categorize the following requirements into functional and non-functional,
        then prioritize them based on business value and technical feasibility:
        
        Requirements: {requirements}
        """
        
        # Simulate Claude Sonnet response
        categorized_requirements = {
            "functional": [
                {"requirement": "Requirement 1", "priority": "high", "business_value": "high", "feasibility": "medium"},
                {"requirement": "Requirement 2", "priority": "medium", "business_value": "medium", "feasibility": "high"}
            ],
            "non_functional": [
                {"requirement": "Performance requirement", "priority": "high", "business_value": "high", "feasibility": "low"},
                {"requirement": "Security requirement", "priority": "high", "business_value": "high", "feasibility": "medium"}
            ]
        }
        
        return categorized_requirements
    
    def specification_generator(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a complete specification document from project data
        """
        # Using Claude Sonnet to generate a comprehensive specification
        spec_prompt = f"""
        Generate a complete project specification document based on the following data:
        
        Objectives: {project_data.get('objectives', [])}
        Requirements: {project_data.get('requirements', {})}
        User Personas: {project_data.get('personas', [])}
        Design Guidelines: {project_data.get('design_guidelines', {})}
        
        The document should include:
        1. Executive summary
        2. Project objectives with success criteria
        3. Detailed requirements (functional and non-functional)
        4. User personas and scenarios
        5. UI/UX guidelines
        6. Constraints and assumptions
        7. Success metrics
        """
        
        # Simulate Claude Sonnet generating the specification
        specification = {
            "executive_summary": "Executive summary of the project",
            "objectives": project_data.get('objectives', []),
            "functional_requirements": project_data.get('requirements', {}).get('functional', []),
            "non_functional_requirements": project_data.get('requirements', {}).get('non_functional', []),
            "user_personas": project_data.get('personas', []),
            "ui_ux_guidelines": project_data.get('design_guidelines', {}),
            "constraints": ["Constraint 1", "Constraint 2"],
            "assumptions": ["Assumption 1", "Assumption 2"],
            "success_metrics": ["Metric 1", "Metric 2"]
        }
        
        return specification
    
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the full specification phase workflow
        """
        # Phase 1: Objective Definition
        project_context = inputs.get("project_description", "") + " " + inputs.get("business_context", "")
        
        # Extract objectives from documents
        if inputs.get("existing_documentation"):
            doc_analysis = self.document_analysis(inputs["existing_documentation"])
            objectives = doc_analysis.get("key_objectives", [])
        else:
            objectives = []
        
        # Phase 2: Requirements Gathering
        requirements = {}
        if inputs.get("existing_documentation"):
            requirements = self.requirements_management_tool(
                doc_analysis.get("functional_requirements", []) + 
                doc_analysis.get("non_functional_requirements", [])
            )
        else:
            stakeholders = inputs.get("stakeholders", [])
            interview_results = self.stakeholder_interview_simulator(stakeholders, project_context)
            
            # Extract requirements from interview results
            all_requirements = []
            for stakeholder_data in interview_results.values():
                all_requirements.extend(stakeholder_data.get("requirements", []))
            
            requirements = self.requirements_management_tool(all_requirements)
        
        # Phase 3: User Scenario Analysis
        user_research = self.user_research_toolkit(project_context)
        
        # Phase 4: UI/UX Guidelines
        design_guidelines = self.design_system_analyzer(
            str(requirements) + " " + str(user_research)
        )
        
        # Generate final specification
        project_data = {
            "objectives": objectives,
            "requirements": requirements,
            "personas": user_research["personas"],
            "design_guidelines": design_guidelines
        }
        
        specification = self.specification_generator(project_data)
        
        # Return results
        result = {
            "project_specification": specification,
            "user_personas": user_research["personas"],
            "user_journeys": user_research["user_journeys"],
            "ui_ux_guidelines": design_guidelines,
            "requirements_traceability": self.create_traceability_matrix(specification, requirements),
            "stakeholder_alignment_report": self.summarize_stakeholder_input(inputs.get("stakeholders", []), project_context)
        }
        
        return result
    
    def create_traceability_matrix(self, specification: Dict[str, Any], requirements: Dict[str, Any]) -> List[Dict[str, str]]:
        """
        Create a traceability matrix linking objectives to requirements
        """
        matrix = []
        for i, obj in enumerate(specification.get("objectives", [])):
            for j, req in enumerate(requirements.get("functional", []) + requirements.get("non_functional", [])):
                matrix.append({
                    "objective": obj,
                    "requirement": req["requirement"],
                    "relationship": "direct" if i == j else "indirect"
                })
        return matrix
    
    def summarize_stakeholder_input(self, stakeholders: List[str], context: str) -> Dict[str, Any]:
        """
        Summarize stakeholder input and alignment
        """
        interview_results = self.stakeholder_interview_simulator(stakeholders, context)
        
        # Analyze alignment between stakeholders
        common_themes = []
        conflicting_points = []
        
        all_requirements = []
        all_concerns = []
        
        for stakeholder, data in interview_results.items():
            all_requirements.extend(data.get("requirements", []))
            all_concerns.extend(data.get("concerns", []))
        
        # Find common themes
        from collections import Counter
        req_counter = Counter(all_requirements)
        common_themes = [item for item, count in req_counter.items() if count > 1]
        
        return {
            "interview_results": interview_results,
            "common_themes": common_themes,
            "alignment_score": 0.8,  # Example alignment score
            "recommendations": ["Recommendation 1", "Recommendation 2"]
        }

# Example usage
if __name__ == "__main__":
    # Initialize the agent
    agent = SpecificationPhaseAgent()
    
    # Example inputs
    inputs = {
        "project_description": "Develop a customer support chat application that integrates with existing CRM systems",
        "stakeholders": ["Product Manager", "Customer Support Team", "IT Department", "End Users"],
        "existing_documentation": "Initial project brief outlining the need for improved customer support response times",
        "business_context": "Company goal to reduce customer support response times by 50% while maintaining quality"
    }
    
    # Execute the agent
    result = agent.execute(inputs)
    
    # Output the results
    print("Project Specification:")
    print(json.dumps(result["project_specification"], indent=2))
    
    print("\nUser Personas:")
    print(json.dumps(result["user_personas"], indent=2))
    
    print("\nUI/UX Guidelines:")
    print(json.dumps(result["ui_ux_guidelines"], indent=2))