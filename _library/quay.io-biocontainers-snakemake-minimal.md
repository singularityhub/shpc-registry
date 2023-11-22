---
layout: container
name:  "quay.io/biocontainers/snakemake-minimal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-minimal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-minimal/container.yaml"
updated_at: "2023-11-22 02:47:06.234889"
latest: "5.18.0--py_0"
container_url: "https://biocontainers.pro/tools/snakemake-minimal"
aliases:
 - "snakemake"
 - "snakemake-bash-completion"
 - "rst2html4.py"
 - "jsonschema"
 - "rst2html5.py"
 - "rst2html.py"
 - "rst2latex.py"
 - "rst2man.py"
 - "rst2odt.py"
 - "rst2odt_prepstyles.py"
versions:
 - "5.9.1--py_0"
 - "5.18.0--py_0"
 - "5.17.0--py_0"
 - "5.16.0--py_0"
 - "5.15.0--py_0"
 - "5.14.0--py_1"
description: "shpc-registry automated BioContainers addition for snakemake-minimal"
config: {"url": "https://biocontainers.pro/tools/snakemake-minimal", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snakemake-minimal", "latest": {"5.18.0--py_0": "sha256:887a52ddbfd7ab338974941c1f699744773652bff7585a5b17884eb81fe8ef21"}, "tags": {"5.9.1--py_0": "sha256:46611f4b19c9f6e11d9a159af8ded402e59d78d24f2dac6fec24210fde8c602c", "5.18.0--py_0": "sha256:887a52ddbfd7ab338974941c1f699744773652bff7585a5b17884eb81fe8ef21", "5.17.0--py_0": "sha256:078abd9fb362f20f870e5af7e84b0fc820b89734b2baaed5d781a2a37b81b44e", "5.16.0--py_0": "sha256:a0b11db100a14b3fc369db17bb097ca78d255f6403284cd104c61f1ae70cea2f", "5.15.0--py_0": "sha256:9e1724dc99a4a8dcf77ceac11748c66778ebf747d4f8bf622bf600c0b86ada5e", "5.14.0--py_1": "sha256:767af568eb20a31325ff128c2df6a507c54a6e2700a08856ed5b593d11b78c1f"}, "docker": "quay.io/biocontainers/snakemake-minimal", "aliases": {"snakemake": "/usr/local/bin/snakemake", "snakemake-bash-completion": "/usr/local/bin/snakemake-bash-completion", "rst2html4.py": "/usr/local/bin/rst2html4.py", "jsonschema": "/usr/local/bin/jsonschema", "rst2html5.py": "/usr/local/bin/rst2html5.py", "rst2html.py": "/usr/local/bin/rst2html.py", "rst2latex.py": "/usr/local/bin/rst2latex.py", "rst2man.py": "/usr/local/bin/rst2man.py", "rst2odt.py": "/usr/local/bin/rst2odt.py", "rst2odt_prepstyles.py": "/usr/local/bin/rst2odt_prepstyles.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-minimal.
shpc-registry automated BioContainers addition for snakemake-minimal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-minimal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-minimal:5.18.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-minimal/5.18.0--py_0
$ module help quay.io/biocontainers/snakemake-minimal/5.18.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-minimal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-minimal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-minimal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-minimal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-minimal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-minimal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake-bash-completion

```bash
$ singularity exec <container> /usr/local/bin/snakemake-bash-completion
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html4.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html5.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2latex.py

```bash
$ singularity exec <container> /usr/local/bin/rst2latex.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2latex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2latex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2man.py

```bash
$ singularity exec <container> /usr/local/bin/rst2man.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2man.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2man.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt.py

```bash
$ singularity exec <container> /usr/local/bin/rst2odt.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt_prepstyles.py

```bash
$ singularity exec <container> /usr/local/bin/rst2odt_prepstyles.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt_prepstyles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt_prepstyles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)