---
layout: container
name:  "ghcr.io/autamus/git"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/git/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/git/container.yaml"
updated_at: "2025-05-25 03:22:08.208333"
latest: "2.35.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/git"
aliases:
 - "git"
 - "git-cvsserver"
 - "git-receive-pack"
 - "git-shell"
 - "git-upload-archive"
 - "git-upload-pack"
versions:
 - "latest"
 - "2.35.2"
description: "Git is software for tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during software development. Its goals include speed, data integrity, and support for distributed, non-linear workflows."
config: {"docker": "ghcr.io/autamus/git", "url": "https://github.com/orgs/autamus/packages/container/package/git", "maintainer": "@vsoch", "description": "Git is software for tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during software development. Its goals include speed, data integrity, and support for distributed, non-linear workflows.", "latest": {"2.35.2": "sha256:8ae721c5a052e3b5b23bfd2e397161f94ab0964808ba5793729b983be6daa142"}, "tags": {"latest": "sha256:8ae721c5a052e3b5b23bfd2e397161f94ab0964808ba5793729b983be6daa142", "2.35.2": "sha256:8ae721c5a052e3b5b23bfd2e397161f94ab0964808ba5793729b983be6daa142"}, "aliases": {"git": "/opt/view/bin/git", "git-cvsserver": "/opt/view/bin/git-cvsserver", "git-receive-pack": "/opt/view/bin/git-receive-pack", "git-shell": "/opt/view/bin/git-shell", "git-upload-archive": "/opt/view/bin/git-upload-archive", "git-upload-pack": "/opt/view/bin/git-upload-pack"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/git.
Git is software for tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during software development. Its goals include speed, data integrity, and support for distributed, non-linear workflows.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/git
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/git:2.35.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/git/2.35.2
$ module help ghcr.io/autamus/git/2.35.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### git-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### git-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### git-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### git-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### git-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### git-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### git

```bash
$ singularity exec <container> /opt/view/bin/git
$ podman run --it --rm --entrypoint /opt/view/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-cvsserver

```bash
$ singularity exec <container> /opt/view/bin/git-cvsserver
$ podman run --it --rm --entrypoint /opt/view/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-receive-pack

```bash
$ singularity exec <container> /opt/view/bin/git-receive-pack
$ podman run --it --rm --entrypoint /opt/view/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-shell

```bash
$ singularity exec <container> /opt/view/bin/git-shell
$ podman run --it --rm --entrypoint /opt/view/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-archive

```bash
$ singularity exec <container> /opt/view/bin/git-upload-archive
$ podman run --it --rm --entrypoint /opt/view/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-pack

```bash
$ singularity exec <container> /opt/view/bin/git-upload-pack
$ podman run --it --rm --entrypoint /opt/view/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
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