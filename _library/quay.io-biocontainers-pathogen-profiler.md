---
layout: container
name:  "quay.io/biocontainers/pathogen-profiler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pathogen-profiler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pathogen-profiler/container.yaml"
updated_at: "2023-04-11 02:38:44.670061"
latest: "2.0.4--pyh7cba7a3_1"
container_url: "https://biocontainers.pro/tools/pathogen-profiler"
aliases:
 - "add_dummy_AD.py"
 - "combine_vcf_variants.py"
 - "delly"
 - "lofreq"
 - "lofreq2_call_pparallel.py"
 - "lofreq2_indel_ovlp.py"
 - "lofreq2_somatic.py"
 - "lofreq2_vcfplot.py"
 - "rename_vcf_chrom.py"
 - "sam_add_rg.pl"
 - "update_version.sh"
 - "gatk"
 - "pilon"
 - "tabix++"
 - "git"
 - "git-cvsserver"
 - "git-receive-pack"
 - "git-shell"
 - "git-upload-archive"
 - "git-upload-pack"
 - "gitk"
versions:
 - "2.0.1--pypyh5e36f6f_0"
 - "2.0.2--pyh7cba7a3_0"
 - "2.0.2--pyh7cba7a3_1"
 - "2.0.4--pyh7cba7a3_0"
 - "2.0.4--pyh7cba7a3_1"
description: "shpc-registry automated BioContainers addition for pathogen-profiler"
config: {"url": "https://biocontainers.pro/tools/pathogen-profiler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pathogen-profiler", "latest": {"2.0.4--pyh7cba7a3_1": "sha256:0a1051d35b54210269bd7d4adab75f7e9fc89148aa26ca0dc1ab29de187232e8"}, "tags": {"2.0.1--pypyh5e36f6f_0": "sha256:05d950e86c0eb0ad8d8294b4a2e4e6ed54366e05fdb4ac57fea4517041fb91c2", "2.0.2--pyh7cba7a3_0": "sha256:43b6643d6e3922b88665fe53839f6498b3e767cac488f5cab16f0f00d7b1b17b", "2.0.2--pyh7cba7a3_1": "sha256:8c16c31c6e029645abacdc1ca9a9b019596b6df6bc9d970beeebe9bec5326a4d", "2.0.4--pyh7cba7a3_0": "sha256:96d2df698f5ed3b3434375e4d44db4d98e4ee599f9a84064163b8621e1ed8a3b", "2.0.4--pyh7cba7a3_1": "sha256:0a1051d35b54210269bd7d4adab75f7e9fc89148aa26ca0dc1ab29de187232e8"}, "docker": "quay.io/biocontainers/pathogen-profiler", "aliases": {"add_dummy_AD.py": "/usr/local/bin/add_dummy_AD.py", "combine_vcf_variants.py": "/usr/local/bin/combine_vcf_variants.py", "delly": "/usr/local/bin/delly", "lofreq": "/usr/local/bin/lofreq", "lofreq2_call_pparallel.py": "/usr/local/bin/lofreq2_call_pparallel.py", "lofreq2_indel_ovlp.py": "/usr/local/bin/lofreq2_indel_ovlp.py", "lofreq2_somatic.py": "/usr/local/bin/lofreq2_somatic.py", "lofreq2_vcfplot.py": "/usr/local/bin/lofreq2_vcfplot.py", "rename_vcf_chrom.py": "/usr/local/bin/rename_vcf_chrom.py", "sam_add_rg.pl": "/usr/local/bin/sam_add_rg.pl", "update_version.sh": "/usr/local/bin/update_version.sh", "gatk": "/usr/local/bin/gatk", "pilon": "/usr/local/bin/pilon", "tabix++": "/usr/local/bin/tabix++", "git": "/usr/local/bin/git", "git-cvsserver": "/usr/local/bin/git-cvsserver", "git-receive-pack": "/usr/local/bin/git-receive-pack", "git-shell": "/usr/local/bin/git-shell", "git-upload-archive": "/usr/local/bin/git-upload-archive", "git-upload-pack": "/usr/local/bin/git-upload-pack", "gitk": "/usr/local/bin/gitk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pathogen-profiler.
shpc-registry automated BioContainers addition for pathogen-profiler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pathogen-profiler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pathogen-profiler:2.0.4--pyh7cba7a3_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pathogen-profiler/2.0.4--pyh7cba7a3_1
$ module help quay.io/biocontainers/pathogen-profiler/2.0.4--pyh7cba7a3_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pathogen-profiler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pathogen-profiler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pathogen-profiler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pathogen-profiler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pathogen-profiler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pathogen-profiler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_dummy_AD.py

```bash
$ singularity exec <container> /usr/local/bin/add_dummy_AD.py
$ podman run --it --rm --entrypoint /usr/local/bin/add_dummy_AD.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_dummy_AD.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_vcf_variants.py

```bash
$ singularity exec <container> /usr/local/bin/combine_vcf_variants.py
$ podman run --it --rm --entrypoint /usr/local/bin/combine_vcf_variants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_vcf_variants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delly

```bash
$ singularity exec <container> /usr/local/bin/delly
$ podman run --it --rm --entrypoint /usr/local/bin/delly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lofreq

```bash
$ singularity exec <container> /usr/local/bin/lofreq
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lofreq2_call_pparallel.py

```bash
$ singularity exec <container> /usr/local/bin/lofreq2_call_pparallel.py
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq2_call_pparallel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq2_call_pparallel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lofreq2_indel_ovlp.py

```bash
$ singularity exec <container> /usr/local/bin/lofreq2_indel_ovlp.py
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq2_indel_ovlp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq2_indel_ovlp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lofreq2_somatic.py

```bash
$ singularity exec <container> /usr/local/bin/lofreq2_somatic.py
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq2_somatic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq2_somatic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lofreq2_vcfplot.py

```bash
$ singularity exec <container> /usr/local/bin/lofreq2_vcfplot.py
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq2_vcfplot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq2_vcfplot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename_vcf_chrom.py

```bash
$ singularity exec <container> /usr/local/bin/rename_vcf_chrom.py
$ podman run --it --rm --entrypoint /usr/local/bin/rename_vcf_chrom.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename_vcf_chrom.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_add_rg.pl

```bash
$ singularity exec <container> /usr/local/bin/sam_add_rg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_version.sh

```bash
$ singularity exec <container> /usr/local/bin/update_version.sh
$ podman run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk

```bash
$ singularity exec <container> /usr/local/bin/gatk
$ podman run --it --rm --entrypoint /usr/local/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilon

```bash
$ singularity exec <container> /usr/local/bin/pilon
$ podman run --it --rm --entrypoint /usr/local/bin/pilon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix++

```bash
$ singularity exec <container> /usr/local/bin/tabix++
$ podman run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git

```bash
$ singularity exec <container> /usr/local/bin/git
$ podman run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-cvsserver

```bash
$ singularity exec <container> /usr/local/bin/git-cvsserver
$ podman run --it --rm --entrypoint /usr/local/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-receive-pack

```bash
$ singularity exec <container> /usr/local/bin/git-receive-pack
$ podman run --it --rm --entrypoint /usr/local/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-shell

```bash
$ singularity exec <container> /usr/local/bin/git-shell
$ podman run --it --rm --entrypoint /usr/local/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-archive

```bash
$ singularity exec <container> /usr/local/bin/git-upload-archive
$ podman run --it --rm --entrypoint /usr/local/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-pack

```bash
$ singularity exec <container> /usr/local/bin/git-upload-pack
$ podman run --it --rm --entrypoint /usr/local/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gitk

```bash
$ singularity exec <container> /usr/local/bin/gitk
$ podman run --it --rm --entrypoint /usr/local/bin/gitk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gitk   -v ${PWD} -w ${PWD} <container> -c " $@"
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