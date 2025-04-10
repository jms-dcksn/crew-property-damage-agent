from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import BraveSearchTool
from pydantic import BaseModel

brave_search_tool = BraveSearchTool()

class DamageReport(BaseModel):
    summary: str
    damageType: str
    severity: str
    estimatedCost: str
    recommendations: str
    conclusion: str

@CrewBase
class ClaimsVisualDamageAssessmentAgentCrew():
    """ClaimsVisualDamageAssessmentAgent crew"""

    @agent
    def image_preprocessing(self) -> Agent:
        return Agent(
            config=self.agents_config['image_preprocessing'],
            tools=[],
        )

    @agent
    def damage_analysis(self) -> Agent:
        return Agent(
            config=self.agents_config['damage_analysis'],
            tools=[],
        )

    @agent
    def cost_estimation(self) -> Agent:
        return Agent(
            config=self.agents_config['cost_estimation'],
            tools=[brave_search_tool],
        )

    @agent
    def metadata_generation(self) -> Agent:
        return Agent(
            config=self.agents_config['metadata_generation'],
            tools=[],
        )

    @agent
    def report_compilation(self) -> Agent:
        return Agent(
            config=self.agents_config['report_compilation'],
            tools=[],
        )


    @task
    def preprocess_image_task(self) -> Task:
        return Task(
            config=self.tasks_config['preprocess_image_task'],
            tools=[],
        )

    @task
    def analyze_damage_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_damage_task'],
            tools=[],
        )

    @task
    def estimate_cost_task(self) -> Task:
        return Task(
            config=self.tasks_config['estimate_cost_task'],
            tools=[],
        )

    @task
    def generate_metadata_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_metadata_task'],
            tools=[],
        )

    @task
    def compile_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['compile_report_task'],
            tools=[],
            output_pydantic=DamageReport,
        )


    @crew
    def crew(self) -> Crew:
        """Creates the ClaimsVisualDamageAssessmentAgent crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
