---
layout: container
name:  "quay.io/biocontainers/nextstrain-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nextstrain-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nextstrain-cli/container.yaml"
updated_at: "2023-08-28 02:40:37.279105"
latest: "7.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/nextstrain-cli"
aliases:
 - "nextstrain"
 - "docutils"
 - "jp.py"
 - "rst2html4.py"
 - "rst2html5.py"
 - "rst2html.py"
 - "rst2latex.py"
 - "rst2man.py"
 - "rst2odt.py"
 - "rst2odt_prepstyles.py"
 - "rst2pseudoxml.py"
versions:
 - "4.2.0--pyhdfd78af_1"
 - "5.0.1--pyhdfd78af_0"
 - "6.0.0--pyhdfd78af_0"
 - "6.1.0.post1--pyhdfd78af_0"
 - "6.0.3--pyhdfd78af_0"
 - "6.2.0--pyhdfd78af_1"
 - "6.2.1--pyhdfd78af_0"
 - "7.0.1--pyhdfd78af_0"
 - "7.1.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for nextstrain-cli"
config: {"url": "https://biocontainers.pro/tools/nextstrain-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nextstrain-cli", "latest": {"7.1.0--pyhdfd78af_0": "sha256:a13ce0c093e0fd3aea3cea6e3123c034c00f0ea2f56e368efca6692eb7ad3ca6"}, "tags": {"4.2.0--pyhdfd78af_1": "sha256:71902449c6f452deb519f63a161f24453565bbc3caad0344b24bb7da8fa2db2f", "5.0.1--pyhdfd78af_0": "sha256:a7fd5d87d83fd364f6d045b2c704aed26bfbeecdf5eac3b6fc631bd1de67341b", "6.0.0--pyhdfd78af_0": "sha256:7e65c48e4446b4d67ff4a24070536a20434d4305ce301b3746744b277e56f3f4", "6.1.0.post1--pyhdfd78af_0": "sha256:a25271bd0490767c69d6a9bd325ba058aa3a4d36a35597b6ebe8add4ae7884f2", "6.0.3--pyhdfd78af_0": "sha256:f708fead7a1bc26638b0b668fdbb042a584884f37ddfd59f9fcf17973a3bcd83", "6.2.0--pyhdfd78af_1": "sha256:a9b8d24a653ec97abe0a2c434de0e27f26e380651a2b05b3dd9fa27f7f5e9368", "6.2.1--pyhdfd78af_0": "sha256:faa5c300c64f359cad8be7fca21f12be8c812bd40dd4dadcdf5c80b078628198", "7.0.1--pyhdfd78af_0": "sha256:49efb460293cbc1ff5bbeba496287db058a2a3684dafc1736a324edf254602ea", "7.1.0--pyhdfd78af_0": "sha256:a13ce0c093e0fd3aea3cea6e3123c034c00f0ea2f56e368efca6692eb7ad3ca6"}, "docker": "quay.io/biocontainers/nextstrain-cli", "aliases": {"nextstrain": "/usr/local/bin/nextstrain", "docutils": "/usr/local/bin/docutils", "jp.py": "/usr/local/bin/jp.py", "rst2html4.py": "/usr/local/bin/rst2html4.py", "rst2html5.py": "/usr/local/bin/rst2html5.py", "rst2html.py": "/usr/local/bin/rst2html.py", "rst2latex.py": "/usr/local/bin/rst2latex.py", "rst2man.py": "/usr/local/bin/rst2man.py", "rst2odt.py": "/usr/local/bin/rst2odt.py", "rst2odt_prepstyles.py": "/usr/local/bin/rst2odt_prepstyles.py", "rst2pseudoxml.py": "/usr/local/bin/rst2pseudoxml.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nextstrain-cli.
shpc-registry automated BioContainers addition for nextstrain-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nextstrain-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nextstrain-cli:7.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nextstrain-cli/7.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/nextstrain-cli/7.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nextstrain-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nextstrain-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nextstrain-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nextstrain-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nextstrain-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nextstrain-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nextstrain

```bash
$ singularity exec <container> /usr/local/bin/nextstrain
$ podman run --it --rm --entrypoint /usr/local/bin/nextstrain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextstrain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html4.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### rst2pseudoxml.py

```bash
$ singularity exec <container> /usr/local/bin/rst2pseudoxml.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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