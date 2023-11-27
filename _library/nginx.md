---
layout: container
name:  "nginx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nginx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/nginx/container.yaml"
updated_at: "2023-11-27 02:28:23.326218"
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
description: "Nginx (pronounced 'engine-x') is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server)."
config: {"docker": "nginx", "url": "https://hub.docker.com/r/_/nginx", "maintainer": "@vsoch", "description": "Nginx (pronounced 'engine-x') is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server).", "latest": {"alpine3.18": "sha256:db353d0f0c479c91bd15e01fc68ed0f33d9c4c52f3415e63332c3d0bf7a4bb77"}, "tags": {"1.20.0-alpine-perl": "sha256:00109feeafcc6b80f2322cf70b406d5e521f53d0b0841acfce22aa2a827115d6", "1.21.0-alpine-perl": "sha256:fea7bc7dc04726dbc2e89457f7548f47c6914714a1a5ec6e50e2a13f10c22378", "1.21.1": "sha256:a05b0cdd4fc1be3b224ba9662ebdf98fe44c09c0c9215b45f84344c12867002e", "1.21.1-alpine-perl": "sha256:14f5b7ec666c31801d2e06312bea48cff2f366d350d3825d29ae92b9d5fbad83", "1.21.3": "sha256:644a70516a26004c97d0d85c7fe1d0c3a67ea8ab7ddf4aff193d9f301670cf36", "1.21.4": "sha256:366e9f1ddebdb844044c2fafd13b75271a9f620819370f8971220c2b330a9254", "1.21.5": "sha256:0d17b565c37bcbd895e9d92315a05c1c3c9a29f762b011a10c54a66cd53c9b31", "1.21.6": "sha256:2bcabc23b45489fb0885d69a06ba1d648aeda973fae7bb981bafbb884165e514", "latest": "sha256:86e53c4c16a6a276b204b0fd3a8143d86547c967dc8258b3d47c3a21bb68d3c6", "stable-alpine-perl": "sha256:b2879c77d21e59ad33635fac8f810e204d30e933527f39f0f8a60dca7562ab69", "1": "sha256:86e53c4c16a6a276b204b0fd3a8143d86547c967dc8258b3d47c3a21bb68d3c6", "1.21": "sha256:2bcabc23b45489fb0885d69a06ba1d648aeda973fae7bb981bafbb884165e514", "1.20": "sha256:38f8c1d9613f3f42e7969c3b1dd5c3277e635d4576713e6453c6193e66270a6d", "1.22": "sha256:fc5f5fb7574755c306aaf88456ebfbe0b006420a184d52b923d2f0197108f6b7", "1.23": "sha256:f5747a42e3adcb3168049d63278d7251d91185bb5111d2563d58729a5c9179b0", "1.24": "sha256:8091c5f722b5060431042b000a742df96a586c6ecc3dcb440fbbdbdc3c261f3e", "1.25": "sha256:86e53c4c16a6a276b204b0fd3a8143d86547c967dc8258b3d47c3a21bb68d3c6", "1.23.4": "sha256:f5747a42e3adcb3168049d63278d7251d91185bb5111d2563d58729a5c9179b0", "1.24.0-bullseye-perl": "sha256:3487434b3141ac6300a36fcef44064012e61d767ce7df88d4d2601256c273777", "alpine3.18": "sha256:db353d0f0c479c91bd15e01fc68ed0f33d9c4c52f3415e63332c3d0bf7a4bb77"}, "aliases": {"nginx": "/usr/sbin/nginx", "nginx-debug": "/usr/sbin/nginx-debug"}}
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