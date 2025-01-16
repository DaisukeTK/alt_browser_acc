PREFIX ?= /data/data/com.termux/files/usr
TARGET = dist/alt_browser_acc

SRC = alt_browser_acc.py
SPEC = alt_browser_acc.spec

BIN_DIR = $(PREFIX)/bin

all: $(TARGET)

$(TARGET): $(SRC)
	pyinstaller --clean --onefile $<

install:
	install -m 755 $(TARGET) $(BIN_DIR)

clean:
	rm -rf $(TARGET) $(SPEC) dist build 

