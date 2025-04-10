#!/usr/bin/env python
import sys
from claims_visual_damage_assessment_agent.crew import ClaimsVisualDamageAssessmentAgentCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'image_url': 'https://storage.googleapis.com/kagglesdsdata/datasets/4304119/7401868/test/Damaged_building/2%20%28447%29.jpeg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20250408%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250408T233946Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=88d4fb0096dc06f9a3cd44a59b8a644f7883e2d9cac0875388278e6b11651cf2ffd69d2fddbe4f74f65134fedf31aab07220bd4353065357f97e90bd62b3b7b4ed54af912cb888942c9eabda7cfdb9781bc7b5ddad3643910ffc1ac52dd130fd7a0c41ec4a566e41111c97b3b57e2045445cb99c0069c75f2e7e37d4fcd579780fc3497d82e8c7de8ca5e6d0255e937f30f506dee9dd496880479085e32f989fecf3a163caea5b51c8b5eb5274cdaf4b59dcc42461e777341990decb089c5c423217c5ae7343ec33f10ae06294269c2732b2436a59ba1b9d2589758ed55df69bebf2861a4a9263f375e054cec75f73e6bcecbb4ccb98f0ceba4d40c9f9dbcf09',
        'inspection_date': '04/07/2025',
        'claim_id': '122929'
    }
    ClaimsVisualDamageAssessmentAgentCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'image_url': 'sample_value',
        'inspection_date': 'sample_value',
        'claim_id': 'sample_value'
    }
    try:
        ClaimsVisualDamageAssessmentAgentCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ClaimsVisualDamageAssessmentAgentCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'image_url': 'sample_value',
        'inspection_date': 'sample_value',
        'claim_id': 'sample_value'
    }
    try:
        ClaimsVisualDamageAssessmentAgentCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
