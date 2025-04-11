---
layout: container
name:  "nginx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nginx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/nginx/container.yaml"
updated_at: "2025-04-11 03:53:26.325057"
latest: "alpine3.18"
container_url: "https://hub.docker.com/r/_/nginx"
aliases:
 - "nginx"
 - "nginx-debug"
versions:
 - "1.20.0-alpine-perl"
 - "1.21.0-alpine-perl"
 - "1.21.1"
 - "1.21.1-alpine-perl"
 - "1.21.3"
 - "1.21.4"
 - "1.21.5"
 - "1.21.6"
 - "latest"
 - "stable-alpine-perl"
 - "1"
 - "1.21"
 - "1.20"
 - "1.22"
 - "1.23"
 - "1.24"
 - "1.25"
 - "1.23.4"
 - "1.24.0-bullseye-perl"
 - "alpine3.18"
 - "1.26"
 - "1.25.5"
 - "1.27"
 - "1.25.5-alpine3.19-otel"
 - "1.26.2"
 - "1.26.2-alpine-otel"
description: "Nginx (pronounced 'engine-x') is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server)."
config: {"docker": "nginx", "url": "https://hub.docker.com/r/_/nginx", "maintainer": "@vsoch", "description": "Nginx (pronounced 'engine-x') is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server).", "latest": {"alpine3.18": "sha256:31bad00311cb5eeb8a6648beadcf67277a175da89989f14727420a80e2e76742"}, "tags": {"1.20.0-alpine-perl": "sha256:00109feeafcc6b80f2322cf70b406d5e521f53d0b0841acfce22aa2a827115d6", "1.21.0-alpine-perl": "sha256:fea7bc7dc04726dbc2e89457f7548f47c6914714a1a5ec6e50e2a13f10c22378", "1.21.1": "sha256:a05b0cdd4fc1be3b224ba9662ebdf98fe44c09c0c9215b45f84344c12867002e", "1.21.1-alpine-perl": "sha256:14f5b7ec666c31801d2e06312bea48cff2f366d350d3825d29ae92b9d5fbad83", "1.21.3": "sha256:644a70516a26004c97d0d85c7fe1d0c3a67ea8ab7ddf4aff193d9f301670cf36", "1.21.4": "sha256:366e9f1ddebdb844044c2fafd13b75271a9f620819370f8971220c2b330a9254", "1.21.5": "sha256:0d17b565c37bcbd895e9d92315a05c1c3c9a29f762b011a10c54a66cd53c9b31", "1.21.6": "sha256:2bcabc23b45489fb0885d69a06ba1d648aeda973fae7bb981bafbb884165e514", "latest": "sha256:09369da6b10306312cd908661320086bf87fbae1b6b0c49a1f50ba531fef2eab", "stable-alpine-perl": "sha256:0166175f93756885810ef49cad18aeb5262a8f75e1674350f6d59301ba9f8688", "1": "sha256:09369da6b10306312cd908661320086bf87fbae1b6b0c49a1f50ba531fef2eab", "1.21": "sha256:2bcabc23b45489fb0885d69a06ba1d648aeda973fae7bb981bafbb884165e514", "1.20": "sha256:38f8c1d9613f3f42e7969c3b1dd5c3277e635d4576713e6453c6193e66270a6d", "1.22": "sha256:fc5f5fb7574755c306aaf88456ebfbe0b006420a184d52b923d2f0197108f6b7", "1.23": "sha256:f5747a42e3adcb3168049d63278d7251d91185bb5111d2563d58729a5c9179b0", "1.24": "sha256:f6daac2445b0ce70e64d77442ccf62839f3f1b4c24bf6746a857eff014e798c8", "1.25": "sha256:a484819eb60211f5299034ac80f6a681b06f89e65866ce91f356ed7c72af059c", "1.23.4": "sha256:f5747a42e3adcb3168049d63278d7251d91185bb5111d2563d58729a5c9179b0", "1.24.0-bullseye-perl": "sha256:fc78d87401fdbadf36c638febdad36ae17dd51d7b5d70bb0a34d94e0daa3a0e1", "alpine3.18": "sha256:31bad00311cb5eeb8a6648beadcf67277a175da89989f14727420a80e2e76742", "1.26": "sha256:41b194461e4bae16f9b25d68b0976ed4735b89ca625c89aad88e1c1c3b7e8860", "1.25.5": "sha256:a484819eb60211f5299034ac80f6a681b06f89e65866ce91f356ed7c72af059c", "1.27": "sha256:09369da6b10306312cd908661320086bf87fbae1b6b0c49a1f50ba531fef2eab", "1.25.5-alpine3.19-otel": "sha256:8e3ecd502317cc9e4f2939b71713cc1e65388cc2dad654a2efca5019b53ddb05", "1.26.2": "sha256:43a626425e38f1d80cd17303c5d44b5f5b22b8b10d0c0f1e50b047cf4e1ad5dd", "1.26.2-alpine-otel": "sha256:cd431e1c871321aee9940c13ec2f1ecc780f9179aa0939ca54e8518bbdf301d8"}, "aliases": {"nginx": "/usr/sbin/nginx", "nginx-debug": "/usr/sbin/nginx-debug"}}
---

This module is a singularity container wrapper for nginx.
Nginx (pronounced 'engine-x') is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server).
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nginx
```

Or a specific version:

```bash
$ shpc install nginx:alpine3.18
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nginx/alpine3.18
$ module help nginx/alpine3.18
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nginx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nginx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nginx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nginx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nginx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nginx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nginx

```bash
$ singularity exec <container> /usr/sbin/nginx
$ podman run --it --rm --entrypoint /usr/sbin/nginx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/sbin/nginx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nginx-debug

```bash
$ singularity exec <container> /usr/sbin/nginx-debug
$ podman run --it --rm --entrypoint /usr/sbin/nginx-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/sbin/nginx-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
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