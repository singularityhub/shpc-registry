---
layout: container
name:  "quay.io/biocontainers/edittag"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/edittag/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/edittag/container.yaml"
updated_at: "2024-01-02 02:47:40.397519"
latest: "1.1--py_2"
container_url: "https://biocontainers.pro/tools/edittag"
aliases:
 - "add_tags_to_adapters.py"
 - "add_tags_to_primers.py"
 - "design_edit_metric_tags.py"
 - "estimate_sequencing_error_effects.py"
 - "get_tag_flows_for_454.py"
 - "validate_edit_metric_tags.py"
 - "f2py3.7"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
 - "pyvenv"
versions:
 - "1.1--py_2"
description: "shpc-registry automated BioContainers addition for edittag"
config: {"url": "https://biocontainers.pro/tools/edittag", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for edittag", "latest": {"1.1--py_2": "sha256:fcbd4abbaa4dab6383a517cc3a36a0032bc0f0e3245d3b920a1457f805da94c1"}, "tags": {"1.1--py_2": "sha256:fcbd4abbaa4dab6383a517cc3a36a0032bc0f0e3245d3b920a1457f805da94c1"}, "docker": "quay.io/biocontainers/edittag", "aliases": {"add_tags_to_adapters.py": "/usr/local/bin/add_tags_to_adapters.py", "add_tags_to_primers.py": "/usr/local/bin/add_tags_to_primers.py", "design_edit_metric_tags.py": "/usr/local/bin/design_edit_metric_tags.py", "estimate_sequencing_error_effects.py": "/usr/local/bin/estimate_sequencing_error_effects.py", "get_tag_flows_for_454.py": "/usr/local/bin/get_tag_flows_for_454.py", "validate_edit_metric_tags.py": "/usr/local/bin/validate_edit_metric_tags.py", "f2py3.7": "/usr/local/bin/f2py3.7", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/edittag.
shpc-registry automated BioContainers addition for edittag
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/edittag
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/edittag:1.1--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/edittag/1.1--py_2
$ module help quay.io/biocontainers/edittag/1.1--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### edittag-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### edittag-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### edittag-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### edittag-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### edittag-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### edittag-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_tags_to_adapters.py

```bash
$ singularity exec <container> /usr/local/bin/add_tags_to_adapters.py
$ podman run --it --rm --entrypoint /usr/local/bin/add_tags_to_adapters.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_tags_to_adapters.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### add_tags_to_primers.py

```bash
$ singularity exec <container> /usr/local/bin/add_tags_to_primers.py
$ podman run --it --rm --entrypoint /usr/local/bin/add_tags_to_primers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_tags_to_primers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design_edit_metric_tags.py

```bash
$ singularity exec <container> /usr/local/bin/design_edit_metric_tags.py
$ podman run --it --rm --entrypoint /usr/local/bin/design_edit_metric_tags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design_edit_metric_tags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimate_sequencing_error_effects.py

```bash
$ singularity exec <container> /usr/local/bin/estimate_sequencing_error_effects.py
$ podman run --it --rm --entrypoint /usr/local/bin/estimate_sequencing_error_effects.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimate_sequencing_error_effects.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_tag_flows_for_454.py

```bash
$ singularity exec <container> /usr/local/bin/get_tag_flows_for_454.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_tag_flows_for_454.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_tag_flows_for_454.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validate_edit_metric_tags.py

```bash
$ singularity exec <container> /usr/local/bin/validate_edit_metric_tags.py
$ podman run --it --rm --entrypoint /usr/local/bin/validate_edit_metric_tags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validate_edit_metric_tags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.7

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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