import os, yaml, datetime

def main():
    # Ensure the PULL_REQUEST_TEMPLATE directory exists
    os.makedirs('.github/PULL_REQUEST_TEMPLATE', exist_ok=True)
    
    with open('templates.yaml') as f:
        templates = yaml.safe_load(f)
    for t in templates:
        name = t.get('name')
        content = t.get('content', '')
        if os.environ.get('INPUT_INJECT_DATE', 'false').lower() == 'true':
            content = content.replace('{{DATE}}', datetime.datetime.utcnow().strftime('%Y-%m-%d'))
        if os.environ.get('INPUT_INJECT_AUTHOR', 'false').lower() == 'true':
            content = content.replace('{{AUTHOR}}', os.environ.get('GITHUB_ACTOR', 'unknown'))
        path = f'.github/PULL_REQUEST_TEMPLATE/{name}'
        if os.path.exists(path) and os.environ.get('INPUT_OVERWRITE', 'false').lower() != 'true':
            print(f'{path} exists. Skipping (overwrite disabled).')
            continue
        # Validation: must have Description and Checklist
        if 'Description' not in content or 'Checklist' not in content:
            print(f'Warning: {name} missing required sections.')
        with open(path, 'w') as out:
            out.write(content)
        print(f'Created/updated {path}')

if __name__ == '__main__':
    main()
