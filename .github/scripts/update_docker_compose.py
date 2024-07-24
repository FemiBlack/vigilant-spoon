import yaml
import sys

def update_docker_compose(compose_file, project_id, short_sha):
    with open(compose_file, 'r') as f:
        data = yaml.safe_load(f)

    for service_name, service in data['services'].items():
        service['image'] = f"gcr.io/{project_id}/{service_name}:{short_sha}"
        if 'build' in service:
            del service['build']

    with open(compose_file, 'w') as f:
        yaml.safe_dump(data, f, default_flow_style=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: update_docker_compose.py <compose_file> <project_id> <short_sha>")
        sys.exit(1)

    compose_file = sys.argv[1]
    project_id = sys.argv[2]
    short_sha = sys.argv[3]

    update_docker_compose(compose_file, project_id, short_sha)
