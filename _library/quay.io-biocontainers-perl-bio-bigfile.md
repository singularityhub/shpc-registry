---
layout: container
name:  "quay.io/biocontainers/perl-bio-bigfile"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-bigfile/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-bigfile/container.yaml"
updated_at: "2025-02-27 03:08:44.093508"
latest: "1.07--pl5321h41f7678_5"
container_url: "https://biocontainers.pro/tools/perl-bio-bigfile"
aliases:
 - "bigWigToWig.pl"
 - "ibd2sdi"
 - "index_bigwigset.pl"
 - "innochecksum"
 - "myisam_ftdump"
 - "myisamchk"
 - "myisamlog"
 - "myisampack"
 - "mysql"
 - "mysql.server"
 - "mysql_config_editor"
 - "mysql_secure_installation"
 - "mysql_ssl_rsa_setup"
 - "mysql_tzinfo_to_sql"
 - "mysql_upgrade"
 - "mysqladmin"
 - "mysqlbinlog"
 - "mysqlcheck"
 - "mysqld"
 - "mysqld_multi"
 - "mysqld_safe"
 - "mysqldump"
 - "mysqldumpslow"
 - "mysqlimport"
 - "mysqlpump"
 - "mysqlshow"
 - "mysqlslap"
 - "wigToBigWig.pl"
 - "zlib_decompress"
 - "bp_pairwise_kaks.pl"
 - "bp_search2BSML.pl"
 - "bp_aacomp.pl"
 - "bp_biofetch_genbank_proxy.pl"
 - "bp_bioflat_index.pl"
 - "bp_biogetseq.pl"
 - "bp_blast2tree.pl"
 - "bp_bulk_load_gff.pl"
 - "bp_chaos_plot.pl"
 - "bp_classify_hits_kingdom.pl"
versions:
 - "1.07--pl526hab1572f_1"
 - "1.07--pl5321h0e0aaa8_3"
 - "1.07--pl5321h84c94e8_4"
 - "1.07--pl5321h41f7678_5"
description: "shpc-registry automated BioContainers addition for perl-bio-bigfile"
config: {"url": "https://biocontainers.pro/tools/perl-bio-bigfile", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bio-bigfile", "latest": {"1.07--pl5321h41f7678_5": "sha256:aa94f9858c56735fd1d0c78acd6e915fee43cbed929a8ad87ee2af497565a984"}, "tags": {"1.07--pl526hab1572f_1": "sha256:1a20db37bc1ba1e679ebe4d6a7483d00263ef17ff2812dd5882ca18d862aaded", "1.07--pl5321h0e0aaa8_3": "sha256:8aec7603ddfb3086d96a0754e4c6198d61deff0a50557afadda578a3ac336dcf", "1.07--pl5321h84c94e8_4": "sha256:2079082675435b5cdf81cb324ef1a4bfcb48187542a7239a8e018e99b5b40ce6", "1.07--pl5321h41f7678_5": "sha256:aa94f9858c56735fd1d0c78acd6e915fee43cbed929a8ad87ee2af497565a984"}, "docker": "quay.io/biocontainers/perl-bio-bigfile", "aliases": {"bigWigToWig.pl": "/usr/local/bin/bigWigToWig.pl", "ibd2sdi": "/usr/local/bin/ibd2sdi", "index_bigwigset.pl": "/usr/local/bin/index_bigwigset.pl", "innochecksum": "/usr/local/bin/innochecksum", "myisam_ftdump": "/usr/local/bin/myisam_ftdump", "myisamchk": "/usr/local/bin/myisamchk", "myisamlog": "/usr/local/bin/myisamlog", "myisampack": "/usr/local/bin/myisampack", "mysql": "/usr/local/bin/mysql", "mysql.server": "/usr/local/bin/mysql.server", "mysql_config_editor": "/usr/local/bin/mysql_config_editor", "mysql_secure_installation": "/usr/local/bin/mysql_secure_installation", "mysql_ssl_rsa_setup": "/usr/local/bin/mysql_ssl_rsa_setup", "mysql_tzinfo_to_sql": "/usr/local/bin/mysql_tzinfo_to_sql", "mysql_upgrade": "/usr/local/bin/mysql_upgrade", "mysqladmin": "/usr/local/bin/mysqladmin", "mysqlbinlog": "/usr/local/bin/mysqlbinlog", "mysqlcheck": "/usr/local/bin/mysqlcheck", "mysqld": "/usr/local/bin/mysqld", "mysqld_multi": "/usr/local/bin/mysqld_multi", "mysqld_safe": "/usr/local/bin/mysqld_safe", "mysqldump": "/usr/local/bin/mysqldump", "mysqldumpslow": "/usr/local/bin/mysqldumpslow", "mysqlimport": "/usr/local/bin/mysqlimport", "mysqlpump": "/usr/local/bin/mysqlpump", "mysqlshow": "/usr/local/bin/mysqlshow", "mysqlslap": "/usr/local/bin/mysqlslap", "wigToBigWig.pl": "/usr/local/bin/wigToBigWig.pl", "zlib_decompress": "/usr/local/bin/zlib_decompress", "bp_pairwise_kaks.pl": "/usr/local/bin/bp_pairwise_kaks.pl", "bp_search2BSML.pl": "/usr/local/bin/bp_search2BSML.pl", "bp_aacomp.pl": "/usr/local/bin/bp_aacomp.pl", "bp_biofetch_genbank_proxy.pl": "/usr/local/bin/bp_biofetch_genbank_proxy.pl", "bp_bioflat_index.pl": "/usr/local/bin/bp_bioflat_index.pl", "bp_biogetseq.pl": "/usr/local/bin/bp_biogetseq.pl", "bp_blast2tree.pl": "/usr/local/bin/bp_blast2tree.pl", "bp_bulk_load_gff.pl": "/usr/local/bin/bp_bulk_load_gff.pl", "bp_chaos_plot.pl": "/usr/local/bin/bp_chaos_plot.pl", "bp_classify_hits_kingdom.pl": "/usr/local/bin/bp_classify_hits_kingdom.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-bigfile.
shpc-registry automated BioContainers addition for perl-bio-bigfile
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-bigfile
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-bigfile:1.07--pl5321h41f7678_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-bigfile/1.07--pl5321h41f7678_5
$ module help quay.io/biocontainers/perl-bio-bigfile/1.07--pl5321h41f7678_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-bigfile-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-bigfile-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-bigfile-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-bigfile-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-bigfile-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-bigfile-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bigWigToWig.pl

```bash
$ singularity exec <container> /usr/local/bin/bigWigToWig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigToWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigToWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibd2sdi

```bash
$ singularity exec <container> /usr/local/bin/ibd2sdi
$ podman run --it --rm --entrypoint /usr/local/bin/ibd2sdi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibd2sdi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_bigwigset.pl

```bash
$ singularity exec <container> /usr/local/bin/index_bigwigset.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_bigwigset.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_bigwigset.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### innochecksum

```bash
$ singularity exec <container> /usr/local/bin/innochecksum
$ podman run --it --rm --entrypoint /usr/local/bin/innochecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/innochecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myisam_ftdump

```bash
$ singularity exec <container> /usr/local/bin/myisam_ftdump
$ podman run --it --rm --entrypoint /usr/local/bin/myisam_ftdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myisam_ftdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myisamchk

```bash
$ singularity exec <container> /usr/local/bin/myisamchk
$ podman run --it --rm --entrypoint /usr/local/bin/myisamchk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myisamchk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myisamlog

```bash
$ singularity exec <container> /usr/local/bin/myisamlog
$ podman run --it --rm --entrypoint /usr/local/bin/myisamlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myisamlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myisampack

```bash
$ singularity exec <container> /usr/local/bin/myisampack
$ podman run --it --rm --entrypoint /usr/local/bin/myisampack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myisampack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql

```bash
$ singularity exec <container> /usr/local/bin/mysql
$ podman run --it --rm --entrypoint /usr/local/bin/mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql.server

```bash
$ singularity exec <container> /usr/local/bin/mysql.server
$ podman run --it --rm --entrypoint /usr/local/bin/mysql.server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql.server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config_editor

```bash
$ singularity exec <container> /usr/local/bin/mysql_config_editor
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config_editor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config_editor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_secure_installation

```bash
$ singularity exec <container> /usr/local/bin/mysql_secure_installation
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_secure_installation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_secure_installation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_ssl_rsa_setup

```bash
$ singularity exec <container> /usr/local/bin/mysql_ssl_rsa_setup
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_tzinfo_to_sql

```bash
$ singularity exec <container> /usr/local/bin/mysql_tzinfo_to_sql
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_tzinfo_to_sql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_tzinfo_to_sql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_upgrade

```bash
$ singularity exec <container> /usr/local/bin/mysql_upgrade
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqladmin

```bash
$ singularity exec <container> /usr/local/bin/mysqladmin
$ podman run --it --rm --entrypoint /usr/local/bin/mysqladmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqladmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlbinlog

```bash
$ singularity exec <container> /usr/local/bin/mysqlbinlog
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlbinlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlbinlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlcheck

```bash
$ singularity exec <container> /usr/local/bin/mysqlcheck
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqld

```bash
$ singularity exec <container> /usr/local/bin/mysqld
$ podman run --it --rm --entrypoint /usr/local/bin/mysqld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqld_multi

```bash
$ singularity exec <container> /usr/local/bin/mysqld_multi
$ podman run --it --rm --entrypoint /usr/local/bin/mysqld_multi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqld_multi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqld_safe

```bash
$ singularity exec <container> /usr/local/bin/mysqld_safe
$ podman run --it --rm --entrypoint /usr/local/bin/mysqld_safe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqld_safe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqldump

```bash
$ singularity exec <container> /usr/local/bin/mysqldump
$ podman run --it --rm --entrypoint /usr/local/bin/mysqldump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqldump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqldumpslow

```bash
$ singularity exec <container> /usr/local/bin/mysqldumpslow
$ podman run --it --rm --entrypoint /usr/local/bin/mysqldumpslow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqldumpslow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlimport

```bash
$ singularity exec <container> /usr/local/bin/mysqlimport
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlimport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlimport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlpump

```bash
$ singularity exec <container> /usr/local/bin/mysqlpump
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlshow

```bash
$ singularity exec <container> /usr/local/bin/mysqlshow
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlshow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlshow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlslap

```bash
$ singularity exec <container> /usr/local/bin/mysqlslap
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlslap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlslap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wigToBigWig.pl

```bash
$ singularity exec <container> /usr/local/bin/wigToBigWig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wigToBigWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wigToBigWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zlib_decompress

```bash
$ singularity exec <container> /usr/local/bin/zlib_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/zlib_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zlib_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_search2BSML.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_search2BSML.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_search2BSML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_search2BSML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_aacomp.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_aacomp.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_aacomp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_aacomp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biofetch_genbank_proxy.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_biofetch_genbank_proxy.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biofetch_genbank_proxy.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biofetch_genbank_proxy.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bioflat_index.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_bioflat_index.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biogetseq.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_biogetseq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biogetseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biogetseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_blast2tree.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_blast2tree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_blast2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_blast2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bulk_load_gff.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_bulk_load_gff.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bulk_load_gff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bulk_load_gff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_chaos_plot.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_chaos_plot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_chaos_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_chaos_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_classify_hits_kingdom.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_classify_hits_kingdom.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_classify_hits_kingdom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_classify_hits_kingdom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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