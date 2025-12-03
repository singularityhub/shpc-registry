---
layout: container
name:  "quay.io/biocontainers/svtyper-python3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svtyper-python3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/svtyper-python3/container.yaml"
updated_at: "2025-12-03 03:38:14.689896"
latest: "0.7.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/svtyper-python3"
aliases:
 - "lib_stats.R"
 - "sv_classifier.py"
 - "svtyper"
 - "svtyper-sso"
 - "update_info.py"
 - "vcf_allele_freq.py"
 - "vcf_group_multiline.py"
 - "vcf_modify_header.py"
 - "vcf_paste.py"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
versions:
 - "0.7.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for svtyper-python3"
config: {"url": "https://biocontainers.pro/tools/svtyper-python3", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for svtyper-python3", "latest": {"0.7.1--pyhdfd78af_0": "sha256:53df7b2f434dabbc6435172b4e50febe59e94f1a439c228373316f6c1743d651"}, "tags": {"0.7.1--pyhdfd78af_0": "sha256:53df7b2f434dabbc6435172b4e50febe59e94f1a439c228373316f6c1743d651"}, "docker": "quay.io/biocontainers/svtyper-python3", "aliases": {"lib_stats.R": "/usr/local/bin/lib_stats.R", "sv_classifier.py": "/usr/local/bin/sv_classifier.py", "svtyper": "/usr/local/bin/svtyper", "svtyper-sso": "/usr/local/bin/svtyper-sso", "update_info.py": "/usr/local/bin/update_info.py", "vcf_allele_freq.py": "/usr/local/bin/vcf_allele_freq.py", "vcf_group_multiline.py": "/usr/local/bin/vcf_group_multiline.py", "vcf_modify_header.py": "/usr/local/bin/vcf_modify_header.py", "vcf_paste.py": "/usr/local/bin/vcf_paste.py", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/svtyper-python3.
singularity registry hpc automated addition for svtyper-python3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svtyper-python3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svtyper-python3:0.7.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svtyper-python3/0.7.1--pyhdfd78af_0
$ module help quay.io/biocontainers/svtyper-python3/0.7.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svtyper-python3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svtyper-python3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svtyper-python3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svtyper-python3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svtyper-python3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svtyper-python3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lib_stats.R

```bash
$ singularity exec <container> /usr/local/bin/lib_stats.R
$ podman run --it --rm --entrypoint /usr/local/bin/lib_stats.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lib_stats.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sv_classifier.py

```bash
$ singularity exec <container> /usr/local/bin/sv_classifier.py
$ podman run --it --rm --entrypoint /usr/local/bin/sv_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sv_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svtyper

```bash
$ singularity exec <container> /usr/local/bin/svtyper
$ podman run --it --rm --entrypoint /usr/local/bin/svtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svtyper-sso

```bash
$ singularity exec <container> /usr/local/bin/svtyper-sso
$ podman run --it --rm --entrypoint /usr/local/bin/svtyper-sso   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svtyper-sso   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_info.py

```bash
$ singularity exec <container> /usr/local/bin/update_info.py
$ podman run --it --rm --entrypoint /usr/local/bin/update_info.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_info.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_allele_freq.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_allele_freq.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_allele_freq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_allele_freq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_group_multiline.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_group_multiline.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_group_multiline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_group_multiline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_modify_header.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_modify_header.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_modify_header.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_modify_header.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_paste.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_paste.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_paste.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_paste.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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