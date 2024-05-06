---
layout: container
name:  "quay.io/biocontainers/perl-html-tidy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-html-tidy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-html-tidy/container.yaml"
updated_at: "2024-05-06 04:32:56.146517"
latest: "1.60--pl5321h031d066_3"
container_url: "https://biocontainers.pro/tools/perl-html-tidy"
aliases:
 - "webtidy"
 - "tidyp"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.60--pl5321hec16e2b_2"
 - "1.60--pl5321h031d066_3"
description: "shpc-registry automated BioContainers addition for perl-html-tidy"
config: {"url": "https://biocontainers.pro/tools/perl-html-tidy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-html-tidy", "latest": {"1.60--pl5321h031d066_3": "sha256:9229c0cd812a606309bdea4d401c358acae404b74fa869864b42332e1df929ce"}, "tags": {"1.60--pl5321hec16e2b_2": "sha256:fc01f4bae989e73eb07fd6c4c6dfc2dacce6c1d3eed6a8fdb21c87f9934ba691", "1.60--pl5321h031d066_3": "sha256:9229c0cd812a606309bdea4d401c358acae404b74fa869864b42332e1df929ce"}, "docker": "quay.io/biocontainers/perl-html-tidy", "aliases": {"webtidy": "/usr/local/bin/webtidy", "tidyp": "/usr/local/bin/tidyp", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-html-tidy.
shpc-registry automated BioContainers addition for perl-html-tidy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-html-tidy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-html-tidy:1.60--pl5321h031d066_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-html-tidy/1.60--pl5321h031d066_3
$ module help quay.io/biocontainers/perl-html-tidy/1.60--pl5321h031d066_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-html-tidy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-html-tidy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-html-tidy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-html-tidy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-html-tidy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-html-tidy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### webtidy

```bash
$ singularity exec <container> /usr/local/bin/webtidy
$ podman run --it --rm --entrypoint /usr/local/bin/webtidy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/webtidy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tidyp

```bash
$ singularity exec <container> /usr/local/bin/tidyp
$ podman run --it --rm --entrypoint /usr/local/bin/tidyp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tidyp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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