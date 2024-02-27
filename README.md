Made this in like 10 minutes lol.

## Calculator Generated With This
(https://github.com/DouglasLiuDev/Brainfuck-Calculator/tree/master)

```C
#include <stdio.h>
#include <conio.h>
char tape[30000];
int ptr = 0;
int main()
{
    tape[ptr] = (tape[ptr] + 1) % 256;
    ++ptr;
    tape[ptr] = (tape[ptr] + 1) % 256;
    ++ptr;
    tape[ptr] = (tape[ptr] + 1) % 256;
    ++ptr;
    tape[ptr] = (tape[ptr] + 1) % 256;
    ++ptr;
    ++ptr;
    ++ptr;
    tape[ptr] = getch();
    printf("%c",tape[ptr]);
    ++ptr;
    tape[ptr] = (tape[ptr] + 1) % 256;
    tape[ptr] = (tape[ptr] + 1) % 256;
    tape[ptr] = (tape[ptr] + 1) % 256;
    tape[ptr] = (tape[ptr] + 1) % 256;
    while (tape[ptr] != 0){
        --ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        }
    --ptr;
    tape[ptr] = (tape[ptr] - 1) % 256;
    tape[ptr] = (tape[ptr] - 1) % 256;
    tape[ptr] = (tape[ptr] - 1) % 256;
    tape[ptr] = (tape[ptr] - 1) % 256;
    tape[ptr] = (tape[ptr] - 1) % 256;
    tape[ptr] = (tape[ptr] - 1) % 256;
    tape[ptr] = (tape[ptr] - 1) % 256;
    while (tape[ptr] != 0){
        tape[ptr] = (tape[ptr] - 1) % 256;
        --ptr;
        while (tape[ptr] != 0){
            ++ptr;
            ++ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        ++ptr;
        ++ptr;
        while (tape[ptr] != 0){
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        while (tape[ptr] != 0){
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        tape[ptr] = getch();
        printf("%c",tape[ptr]);
        ++ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        while (tape[ptr] != 0){
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        while (tape[ptr] != 0){
            ++ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        ++ptr;
        while (tape[ptr] != 0){
            --ptr;
            --ptr;
            --ptr;
            --ptr;
            --ptr;
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            ++ptr;
            ++ptr;
            ++ptr;
            ++ptr;
            ++ptr;
            ++ptr;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            while (tape[ptr] != 0){
                --ptr;
                --ptr;
                --ptr;
                --ptr;
                --ptr;
                --ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                ++ptr;
                ++ptr;
                ++ptr;
                ++ptr;
                ++ptr;
                ++ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                tape[ptr] = (tape[ptr] - 1) % 256;
                while (tape[ptr] != 0){
                    --ptr;
                    --ptr;
                    --ptr;
                    --ptr;
                    --ptr;
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    ++ptr;
                    ++ptr;
                    ++ptr;
                    ++ptr;
                    ++ptr;
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    while (tape[ptr] != 0){
                        --ptr;
                        --ptr;
                        --ptr;
                        --ptr;
                        --ptr;
                        --ptr;
                        --ptr;
                        tape[ptr] = (tape[ptr] + 1) % 256;
                        ++ptr;
                        tape[ptr] = (tape[ptr] + 1) % 256;
                        ++ptr;
                        tape[ptr] = (tape[ptr] + 1) % 256;
                        ++ptr;
                        ++ptr;
                        ++ptr;
                        ++ptr;
                        ++ptr;
                        while (tape[ptr] != 0){
                            --ptr;
                            tape[ptr] = (tape[ptr] + 1) % 256;
                            ++ptr;
                            tape[ptr] = (tape[ptr] - 1) % 256;
                            }
                        }
                    }
                }
            }
        --ptr;
        }
    ++ptr;
    tape[ptr] = getch();
    printf("%c",tape[ptr]);
    ++ptr;
    tape[ptr] = (tape[ptr] + 1) % 256;
    tape[ptr] = (tape[ptr] + 1) % 256;
    tape[ptr] = (tape[ptr] + 1) % 256;
    tape[ptr] = (tape[ptr] + 1) % 256;
    while (tape[ptr] != 0){
        --ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        }
    --ptr;
    tape[ptr] = (tape[ptr] - 1) % 256;
    tape[ptr] = (tape[ptr] - 1) % 256;
    tape[ptr] = (tape[ptr] - 1) % 256;
    tape[ptr] = (tape[ptr] - 1) % 256;
    tape[ptr] = (tape[ptr] - 1) % 256;
    tape[ptr] = (tape[ptr] - 1) % 256;
    tape[ptr] = (tape[ptr] - 1) % 256;
    while (tape[ptr] != 0){
        tape[ptr] = (tape[ptr] - 1) % 256;
        --ptr;
        while (tape[ptr] != 0){
            ++ptr;
            ++ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        ++ptr;
        ++ptr;
        while (tape[ptr] != 0){
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        while (tape[ptr] != 0){
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        tape[ptr] = getch();
        printf("%c",tape[ptr]);
        ++ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        while (tape[ptr] != 0){
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            tape[ptr] = (tape[ptr] - 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        tape[ptr] = (tape[ptr] - 1) % 256;
        while (tape[ptr] != 0){
            ++ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        ++ptr;
        ++ptr;
        while (tape[ptr] != 0){
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        while (tape[ptr] != 0){
            tape[ptr] = (tape[ptr] - 1) % 256;
            while (tape[ptr] != 0){
                tape[ptr] = (tape[ptr] - 1) % 256;
                while (tape[ptr] != 0){
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    while (tape[ptr] != 0){
                        tape[ptr] = (tape[ptr] - 1) % 256;
                        while (tape[ptr] != 0){
                            tape[ptr] = (tape[ptr] - 1) % 256;
                            while (tape[ptr] != 0){
                                tape[ptr] = (tape[ptr] - 1) % 256;
                                while (tape[ptr] != 0){
                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                    while (tape[ptr] != 0){
                                        tape[ptr] = (tape[ptr] - 1) % 256;
                                        while (tape[ptr] != 0){
                                            tape[ptr] = (tape[ptr] - 1) % 256;
                                            while (tape[ptr] != 0){
                                                --ptr;
                                                while (tape[ptr] != 0){
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    }
                                                ++ptr;
                                                while (tape[ptr] != 0){
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        --ptr;
        }
    --ptr;
    --ptr;
    --ptr;
    --ptr;
    --ptr;
    --ptr;
    --ptr;
    while (tape[ptr] != 0){
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        ++ptr;
        while (tape[ptr] != 0){
            ++ptr;
            ++ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        ++ptr;
        while (tape[ptr] != 0){
            ++ptr;
            while (tape[ptr] != 0){
                --ptr;
                --ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                ++ptr;
                ++ptr;
                ++ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                --ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            ++ptr;
            while (tape[ptr] != 0){
                --ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                ++ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        ++ptr;
        while (tape[ptr] != 0){
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        --ptr;
        --ptr;
        --ptr;
        --ptr;
        --ptr;
        --ptr;
        }
    ++ptr;
    while (tape[ptr] != 0){
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        ++ptr;
        ++ptr;
        while (tape[ptr] != 0){
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        --ptr;
        --ptr;
        --ptr;
        --ptr;
        }
    ++ptr;
    while (tape[ptr] != 0){
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        ++ptr;
        ++ptr;
        while (tape[ptr] != 0){
            ++ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        ++ptr;
        ++ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        --ptr;
        while (tape[ptr] != 0){
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            --ptr;
            while (tape[ptr] != 0){
                --ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                ++ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            }
        ++ptr;
        while (tape[ptr] != 0){
            tape[ptr] = (tape[ptr] - 1) % 256;
            --ptr;
            --ptr;
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            ++ptr;
            while (tape[ptr] != 0){
                ++ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                --ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            ++ptr;
            ++ptr;
            ++ptr;
            }
        --ptr;
        --ptr;
        --ptr;
        while (tape[ptr] != 0){
            tape[ptr] = (tape[ptr] - 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            while (tape[ptr] != 0){
                ++ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                --ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            ++ptr;
            ++ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            --ptr;
            while (tape[ptr] != 0){
                ++ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                --ptr;
                while (tape[ptr] != 0){
                    --ptr;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    ++ptr;
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    }
                }
            ++ptr;
            while (tape[ptr] != 0){
                tape[ptr] = (tape[ptr] - 1) % 256;
                --ptr;
                --ptr;
                --ptr;
                --ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                ++ptr;
                while (tape[ptr] != 0){
                    ++ptr;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    --ptr;
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    }
                ++ptr;
                ++ptr;
                ++ptr;
                }
            --ptr;
            --ptr;
            --ptr;
            }
        ++ptr;
        while (tape[ptr] != 0){
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        --ptr;
        --ptr;
        --ptr;
        }
    ++ptr;
    while (tape[ptr] != 0){
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        ++ptr;
        ++ptr;
        ++ptr;
        ++ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        while (tape[ptr] != 0){
            tape[ptr] = (tape[ptr] - 1) % 256;
            --ptr;
            --ptr;
            --ptr;
            while (tape[ptr] != 0){
                ++ptr;
                ++ptr;
                ++ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                ++ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                --ptr;
                --ptr;
                --ptr;
                --ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            ++ptr;
            ++ptr;
            ++ptr;
            while (tape[ptr] != 0){
                --ptr;
                --ptr;
                --ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                ++ptr;
                ++ptr;
                ++ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            --ptr;
            --ptr;
            while (tape[ptr] != 0){
                ++ptr;
                ++ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                ++ptr;
                ++ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                --ptr;
                --ptr;
                --ptr;
                --ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            ++ptr;
            ++ptr;
            while (tape[ptr] != 0){
                --ptr;
                --ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                ++ptr;
                ++ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            ++ptr;
            while (tape[ptr] != 0){
                tape[ptr] = (tape[ptr] - 1) % 256;
                ++ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                ++ptr;
                ++ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                --ptr;
                --ptr;
                while (tape[ptr] != 0){
                    ++ptr;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    --ptr;
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    }
                ++ptr;
                while (tape[ptr] != 0){
                    ++ptr;
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    --ptr;
                    while (tape[ptr] != 0){
                        --ptr;
                        tape[ptr] = (tape[ptr] + 1) % 256;
                        ++ptr;
                        tape[ptr] = (tape[ptr] - 1) % 256;
                        }
                    }
                ++ptr;
                while (tape[ptr] != 0){
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    --ptr;
                    --ptr;
                    --ptr;
                    --ptr;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    --ptr;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    --ptr;
                    --ptr;
                    while (tape[ptr] != 0){
                        tape[ptr] = (tape[ptr] - 1) % 256;
                        }
                    ++ptr;
                    ++ptr;
                    ++ptr;
                    ++ptr;
                    while (tape[ptr] != 0){
                        --ptr;
                        --ptr;
                        --ptr;
                        --ptr;
                        tape[ptr] = (tape[ptr] + 1) % 256;
                        ++ptr;
                        ++ptr;
                        ++ptr;
                        ++ptr;
                        tape[ptr] = (tape[ptr] - 1) % 256;
                        }
                    ++ptr;
                    ++ptr;
                    ++ptr;
                    }
                --ptr;
                --ptr;
                --ptr;
                }
            ++ptr;
            while (tape[ptr] != 0){
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            --ptr;
            --ptr;
            }
        --ptr;
        --ptr;
        while (tape[ptr] != 0){
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        while (tape[ptr] != 0){
            ++ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        ++ptr;
        ++ptr;
        while (tape[ptr] != 0){
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        --ptr;
        --ptr;
        --ptr;
        }
    ++ptr;
    ++ptr;
    ++ptr;
    while (tape[ptr] != 0){
        ++ptr;
        ++ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        while (tape[ptr] != 0){
            --ptr;
            --ptr;
            while (tape[ptr] != 0){
                ++ptr;
                ++ptr;
                ++ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                ++ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                --ptr;
                --ptr;
                --ptr;
                --ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            ++ptr;
            ++ptr;
            ++ptr;
            ++ptr;
            while (tape[ptr] != 0){
                --ptr;
                --ptr;
                --ptr;
                --ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                ++ptr;
                ++ptr;
                ++ptr;
                ++ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            tape[ptr] = (tape[ptr] + 1) % 256;
            --ptr;
            while (tape[ptr] != 0){
                tape[ptr] = (tape[ptr] - 1) % 256;
                while (tape[ptr] != 0){
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    while (tape[ptr] != 0){
                        tape[ptr] = (tape[ptr] - 1) % 256;
                        while (tape[ptr] != 0){
                            tape[ptr] = (tape[ptr] - 1) % 256;
                            while (tape[ptr] != 0){
                                tape[ptr] = (tape[ptr] - 1) % 256;
                                while (tape[ptr] != 0){
                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                    while (tape[ptr] != 0){
                                        tape[ptr] = (tape[ptr] - 1) % 256;
                                        while (tape[ptr] != 0){
                                            tape[ptr] = (tape[ptr] - 1) % 256;
                                            while (tape[ptr] != 0){
                                                tape[ptr] = (tape[ptr] - 1) % 256;
                                                while (tape[ptr] != 0){
                                                    ++ptr;
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    --ptr;
                                                    --ptr;
                                                    --ptr;
                                                    --ptr;
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    ++ptr;
                                                    tape[ptr] = (tape[ptr] + 1) % 256;
                                                    ++ptr;
                                                    ++ptr;
                                                    while (tape[ptr] != 0){
                                                        tape[ptr] = (tape[ptr] - 1) % 256;
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            ++ptr;
            while (tape[ptr] != 0){
                tape[ptr] = (tape[ptr] - 1) % 256;
                ++ptr;
                while (tape[ptr] != 0){
                    ++ptr;
                    }
                ++ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                while (tape[ptr] != 0){
                    --ptr;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    ++ptr;
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    }
                --ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                while (tape[ptr] != 0){
                    --ptr;
                    }
                --ptr;
                --ptr;
                --ptr;
                --ptr;
                while (tape[ptr] != 0){
                    ++ptr;
                    ++ptr;
                    ++ptr;
                    ++ptr;
                    ++ptr;
                    while (tape[ptr] != 0){
                        ++ptr;
                        }
                    --ptr;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    while (tape[ptr] != 0){
                        --ptr;
                        }
                    --ptr;
                    --ptr;
                    --ptr;
                    --ptr;
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    }
                ++ptr;
                ++ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                --ptr;
                while (tape[ptr] != 0){
                    ++ptr;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    --ptr;
                    while (tape[ptr] != 0){
                        --ptr;
                        tape[ptr] = (tape[ptr] + 1) % 256;
                        ++ptr;
                        tape[ptr] = (tape[ptr] - 1) % 256;
                        }
                    }
                ++ptr;
                ++ptr;
                ++ptr;
                }
            --ptr;
            --ptr;
            }
        ++ptr;
        ++ptr;
        ++ptr;
        while (tape[ptr] != 0){
            ++ptr;
            }
        ++ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        while (tape[ptr] != 0){
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        ++ptr;
        ++ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        while (tape[ptr] != 0){
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        ++ptr;
        ++ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        while (tape[ptr] != 0){
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        while (tape[ptr] != 0){
            --ptr;
            }
        --ptr;
        --ptr;
        --ptr;
        --ptr;
        }
    ++ptr;
    tape[ptr] = (tape[ptr] + 1) % 256;
    while (tape[ptr] != 0){
        --ptr;
        --ptr;
        while (tape[ptr] != 0){
            ++ptr;
            ++ptr;
            ++ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            --ptr;
            --ptr;
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        ++ptr;
        ++ptr;
        ++ptr;
        ++ptr;
        while (tape[ptr] != 0){
            --ptr;
            --ptr;
            --ptr;
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            ++ptr;
            ++ptr;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        tape[ptr] = (tape[ptr] + 1) % 256;
        --ptr;
        while (tape[ptr] != 0){
            tape[ptr] = (tape[ptr] - 1) % 256;
            while (tape[ptr] != 0){
                tape[ptr] = (tape[ptr] - 1) % 256;
                while (tape[ptr] != 0){
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    while (tape[ptr] != 0){
                        tape[ptr] = (tape[ptr] - 1) % 256;
                        while (tape[ptr] != 0){
                            tape[ptr] = (tape[ptr] - 1) % 256;
                            while (tape[ptr] != 0){
                                tape[ptr] = (tape[ptr] - 1) % 256;
                                while (tape[ptr] != 0){
                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                    while (tape[ptr] != 0){
                                        tape[ptr] = (tape[ptr] - 1) % 256;
                                        while (tape[ptr] != 0){
                                            tape[ptr] = (tape[ptr] - 1) % 256;
                                            while (tape[ptr] != 0){
                                                ++ptr;
                                                tape[ptr] = (tape[ptr] - 1) % 256;
                                                --ptr;
                                                --ptr;
                                                --ptr;
                                                --ptr;
                                                tape[ptr] = (tape[ptr] - 1) % 256;
                                                tape[ptr] = (tape[ptr] - 1) % 256;
                                                tape[ptr] = (tape[ptr] - 1) % 256;
                                                tape[ptr] = (tape[ptr] - 1) % 256;
                                                tape[ptr] = (tape[ptr] - 1) % 256;
                                                tape[ptr] = (tape[ptr] - 1) % 256;
                                                tape[ptr] = (tape[ptr] - 1) % 256;
                                                tape[ptr] = (tape[ptr] - 1) % 256;
                                                tape[ptr] = (tape[ptr] - 1) % 256;
                                                tape[ptr] = (tape[ptr] - 1) % 256;
                                                ++ptr;
                                                tape[ptr] = (tape[ptr] + 1) % 256;
                                                ++ptr;
                                                ++ptr;
                                                while (tape[ptr] != 0){
                                                    tape[ptr] = (tape[ptr] - 1) % 256;
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        ++ptr;
        while (tape[ptr] != 0){
            tape[ptr] = (tape[ptr] - 1) % 256;
            ++ptr;
            ++ptr;
            while (tape[ptr] != 0){
                ++ptr;
                }
            ++ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            while (tape[ptr] != 0){
                --ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                tape[ptr] = (tape[ptr] + 1) % 256;
                ++ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            while (tape[ptr] != 0){
                --ptr;
                }
            --ptr;
            --ptr;
            --ptr;
            --ptr;
            --ptr;
            while (tape[ptr] != 0){
                ++ptr;
                ++ptr;
                ++ptr;
                ++ptr;
                ++ptr;
                ++ptr;
                while (tape[ptr] != 0){
                    ++ptr;
                    }
                --ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                while (tape[ptr] != 0){
                    --ptr;
                    }
                --ptr;
                --ptr;
                --ptr;
                --ptr;
                --ptr;
                tape[ptr] = (tape[ptr] - 1) % 256;
                }
            ++ptr;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            --ptr;
            while (tape[ptr] != 0){
                ++ptr;
                tape[ptr] = (tape[ptr] + 1) % 256;
                --ptr;
                while (tape[ptr] != 0){
                    --ptr;
                    tape[ptr] = (tape[ptr] + 1) % 256;
                    ++ptr;
                    tape[ptr] = (tape[ptr] - 1) % 256;
                    }
                }
            ++ptr;
            ++ptr;
            ++ptr;
            }
        --ptr;
        --ptr;
        }
    --ptr;
    --ptr;
    --ptr;
    while (tape[ptr] != 0){
        tape[ptr] = (tape[ptr] - 1) % 256;
        ++ptr;
        ++ptr;
        ++ptr;
        ++ptr;
        ++ptr;
        ++ptr;
        ++ptr;
        while (tape[ptr] != 0){
            ++ptr;
            }
        ++ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        while (tape[ptr] != 0){
            --ptr;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            tape[ptr] = (tape[ptr] + 1) % 256;
            ++ptr;
            tape[ptr] = (tape[ptr] - 1) % 256;
            }
        --ptr;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        tape[ptr] = (tape[ptr] + 1) % 256;
        while (tape[ptr] != 0){
            --ptr;
            }
        --ptr;
        --ptr;
        --ptr;
        --ptr;
        --ptr;
        --ptr;
        }
    ++ptr;
    ++ptr;
    ++ptr;
    ++ptr;
    ++ptr;
    ++ptr;
    ++ptr;
    while (tape[ptr] != 0){
        ++ptr;
        }
    --ptr;
    while (tape[ptr] != 0){
        printf("%c",tape[ptr]);
        --ptr;
        }
}
```
