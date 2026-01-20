---
layout: container
name:  "quay.io/biocontainers/arvados-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/arvados-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/arvados-cli/container.yaml"
updated_at: "2026-01-20 04:16:27.061268"
latest: "0.1.20151207150126--0"
container_url: "https://biocontainers.pro/tools/arvados-cli"
aliases:
 - "arv"
 - "arv-crunch-job"
 - "arv-run-pipeline-instance"
 - "arv-tag"
 - "google-api"
 - "launchy"
 - "erb"
 - "gem"
 - "irb"
 - "rake"
 - "rdoc"
 - "ri"
 - "ruby"
 - "easy_install-3.5"
 - "2to3-3.5"
 - "idle3.5"
versions:
 - "0.1.20151207150126--0"
description: "shpc-registry automated BioContainers addition for arvados-cli"
config: {"url": "https://biocontainers.pro/tools/arvados-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for arvados-cli", "latest": {"0.1.20151207150126--0": "sha256:32f7c5728300e118a11b58df80c39dd423c9330b7572b9ae37d051549d6b3cf0"}, "tags": {"0.1.20151207150126--0": "sha256:32f7c5728300e118a11b58df80c39dd423c9330b7572b9ae37d051549d6b3cf0"}, "docker": "quay.io/biocontainers/arvados-cli", "aliases": {"arv": "/usr/local/bin/arv", "arv-crunch-job": "/usr/local/bin/arv-crunch-job", "arv-run-pipeline-instance": "/usr/local/bin/arv-run-pipeline-instance", "arv-tag": "/usr/local/bin/arv-tag", "google-api": "/usr/local/bin/google-api", "launchy": "/usr/local/bin/launchy", "erb": "/usr/local/bin/erb", "gem": "/usr/local/bin/gem", "irb": "/usr/local/bin/irb", "rake": "/usr/local/bin/rake", "rdoc": "/usr/local/bin/rdoc", "ri": "/usr/local/bin/ri", "ruby": "/usr/local/bin/ruby", "easy_install-3.5": "/usr/local/bin/easy_install-3.5", "2to3-3.5": "/usr/local/bin/2to3-3.5", "idle3.5": "/usr/local/bin/idle3.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/arvados-cli.
shpc-registry automated BioContainers addition for arvados-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/arvados-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/arvados-cli:0.1.20151207150126--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/arvados-cli/0.1.20151207150126--0
$ module help quay.io/biocontainers/arvados-cli/0.1.20151207150126--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arvados-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arvados-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arvados-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arvados-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arvados-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arvados-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### arv

```bash
$ singularity exec <container> /usr/local/bin/arv
$ podman run --it --rm --entrypoint /usr/local/bin/arv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-crunch-job

```bash
$ singularity exec <container> /usr/local/bin/arv-crunch-job
$ podman run --it --rm --entrypoint /usr/local/bin/arv-crunch-job   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-crunch-job   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-run-pipeline-instance

```bash
$ singularity exec <container> /usr/local/bin/arv-run-pipeline-instance
$ podman run --it --rm --entrypoint /usr/local/bin/arv-run-pipeline-instance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-run-pipeline-instance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-tag

```bash
$ singularity exec <container> /usr/local/bin/arv-tag
$ podman run --it --rm --entrypoint /usr/local/bin/arv-tag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-tag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google-api

```bash
$ singularity exec <container> /usr/local/bin/google-api
$ podman run --it --rm --entrypoint /usr/local/bin/google-api   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google-api   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### launchy

```bash
$ singularity exec <container> /usr/local/bin/launchy
$ podman run --it --rm --entrypoint /usr/local/bin/launchy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/launchy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### erb

```bash
$ singularity exec <container> /usr/local/bin/erb
$ podman run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem

```bash
$ singularity exec <container> /usr/local/bin/gem
$ podman run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irb

```bash
$ singularity exec <container> /usr/local/bin/irb
$ podman run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rake

```bash
$ singularity exec <container> /usr/local/bin/rake
$ podman run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdoc

```bash
$ singularity exec <container> /usr/local/bin/rdoc
$ podman run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ri

```bash
$ singularity exec <container> /usr/local/bin/ri
$ podman run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ruby

```bash
$ singularity exec <container> /usr/local/bin/ruby
$ podman run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.5

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.5

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.5

```bash
$ singularity exec <container> /usr/local/bin/idle3.5
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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