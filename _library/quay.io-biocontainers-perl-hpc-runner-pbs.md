---
layout: container
name:  "quay.io/biocontainers/perl-hpc-runner-pbs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-hpc-runner-pbs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-hpc-runner-pbs/container.yaml"
updated_at: "2024-01-08 02:55:26.508893"
latest: "0.12--0"
container_url: "https://biocontainers.pro/tools/perl-hpc-runner-pbs"
aliases:
 - "cpus.in"
 - "cpus.pl"
 - "pbsrunner.pl"
 - "slurmrunner.pl"
 - "slurmrunnerbasic.pl"
 - "slurmrunnerrsyslog.pl"
 - "testnodes.pl"
 - "findrule"
 - "l4p-tmpl"
 - "perl5.22.0"
 - "c2ph"
 - "pstruct"
 - "tpage"
 - "ttree"
 - "moose-outdated"
 - "package-stash-conflicts"
 - "podselect"
versions:
 - "0.12--0"
description: "shpc-registry automated BioContainers addition for perl-hpc-runner-pbs"
config: {"url": "https://biocontainers.pro/tools/perl-hpc-runner-pbs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-hpc-runner-pbs", "latest": {"0.12--0": "sha256:ebe8cdeddd845bef8d94a212cc60e553494267055a1144461758012f3ec2b65d"}, "tags": {"0.12--0": "sha256:ebe8cdeddd845bef8d94a212cc60e553494267055a1144461758012f3ec2b65d"}, "docker": "quay.io/biocontainers/perl-hpc-runner-pbs", "aliases": {"cpus.in": "/usr/local/bin/cpus.in", "cpus.pl": "/usr/local/bin/cpus.pl", "pbsrunner.pl": "/usr/local/bin/pbsrunner.pl", "slurmrunner.pl": "/usr/local/bin/slurmrunner.pl", "slurmrunnerbasic.pl": "/usr/local/bin/slurmrunnerbasic.pl", "slurmrunnerrsyslog.pl": "/usr/local/bin/slurmrunnerrsyslog.pl", "testnodes.pl": "/usr/local/bin/testnodes.pl", "findrule": "/usr/local/bin/findrule", "l4p-tmpl": "/usr/local/bin/l4p-tmpl", "perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "tpage": "/usr/local/bin/tpage", "ttree": "/usr/local/bin/ttree", "moose-outdated": "/usr/local/bin/moose-outdated", "package-stash-conflicts": "/usr/local/bin/package-stash-conflicts", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-hpc-runner-pbs.
shpc-registry automated BioContainers addition for perl-hpc-runner-pbs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-hpc-runner-pbs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-hpc-runner-pbs:0.12--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-hpc-runner-pbs/0.12--0
$ module help quay.io/biocontainers/perl-hpc-runner-pbs/0.12--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-hpc-runner-pbs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-hpc-runner-pbs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-hpc-runner-pbs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-hpc-runner-pbs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-hpc-runner-pbs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-hpc-runner-pbs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cpus.in

```bash
$ singularity exec <container> /usr/local/bin/cpus.in
$ podman run --it --rm --entrypoint /usr/local/bin/cpus.in   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpus.in   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpus.pl

```bash
$ singularity exec <container> /usr/local/bin/cpus.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cpus.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpus.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbsrunner.pl

```bash
$ singularity exec <container> /usr/local/bin/pbsrunner.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pbsrunner.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbsrunner.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slurmrunner.pl

```bash
$ singularity exec <container> /usr/local/bin/slurmrunner.pl
$ podman run --it --rm --entrypoint /usr/local/bin/slurmrunner.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slurmrunner.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slurmrunnerbasic.pl

```bash
$ singularity exec <container> /usr/local/bin/slurmrunnerbasic.pl
$ podman run --it --rm --entrypoint /usr/local/bin/slurmrunnerbasic.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slurmrunnerbasic.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slurmrunnerrsyslog.pl

```bash
$ singularity exec <container> /usr/local/bin/slurmrunnerrsyslog.pl
$ podman run --it --rm --entrypoint /usr/local/bin/slurmrunnerrsyslog.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slurmrunnerrsyslog.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testnodes.pl

```bash
$ singularity exec <container> /usr/local/bin/testnodes.pl
$ podman run --it --rm --entrypoint /usr/local/bin/testnodes.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testnodes.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findrule

```bash
$ singularity exec <container> /usr/local/bin/findrule
$ podman run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### l4p-tmpl

```bash
$ singularity exec <container> /usr/local/bin/l4p-tmpl
$ podman run --it --rm --entrypoint /usr/local/bin/l4p-tmpl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/l4p-tmpl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tpage

```bash
$ singularity exec <container> /usr/local/bin/tpage
$ podman run --it --rm --entrypoint /usr/local/bin/tpage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tpage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttree

```bash
$ singularity exec <container> /usr/local/bin/ttree
$ podman run --it --rm --entrypoint /usr/local/bin/ttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moose-outdated

```bash
$ singularity exec <container> /usr/local/bin/moose-outdated
$ podman run --it --rm --entrypoint /usr/local/bin/moose-outdated   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moose-outdated   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### package-stash-conflicts

```bash
$ singularity exec <container> /usr/local/bin/package-stash-conflicts
$ podman run --it --rm --entrypoint /usr/local/bin/package-stash-conflicts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/package-stash-conflicts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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