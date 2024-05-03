from ._anvil_designer import HomeTemplate
from anvil import *


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    open_form('Home')
    pass

  def btn_sap_xep_click(self, **event_args):
    nhap_lieu = self.nhap_so.text.split(",")
    so_nguyen = [int(x) for x in nhap_lieu]

  # Lấy thuật toán được chọn
    thuat_toan = self.chon_thuat_toan.selected_value

  # Sắp xếp dãy số theo thuật toán đã chọn
    if thuat_toan == "Insertion Sort":
      so_nguyen = insertion_sort(so_nguyen)
    elif thuat_toan == "Selection Sort":
      so_nguyen = selection_sort(so_nguyen)
    elif thuat_toan == "Bubble Sort":
      so_nguyen = bubble_sort(so_nguyen)
    elif thuat_toan == "Merge Sort":
      so_nguyen = merge_sort(so_nguyen)
    else:
      print("Lựa chọn thuật toán không hợp lệ!")

  # Hiển thị kết quả
    self.ket_qua.text = ", ".join(str(x) for x in so_nguyen)
  pass
def insertion_sort(a):
  """Hàm sắp xếp Insertion Sort."""
  for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = key
  return a

def selection_sort(a):
  """Hàm sắp xếp Selection Sort."""
  for i in range(len(a) - 1):
    min_index = i
    for j in range(i + 1, len(a)):
      if a[j] < a[min_index]:
        min_index = j
    a[i], a[min_index] = a[min_index], a[i]
  return a

def bubble_sort(a):
  """Hàm sắp xếp Bubble Sort."""
  for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
      if a[j] > a[j + 1]:
        a[j], a[j + 1] = a[j + 1], a[j]
  return a
def merge(left, right):
  """Hàm kết hợp hai mảng đã được sắp xếp."""
  result = []
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  result += left[i:]
  result += right[j:]
  return result

def merge_sort(a):
  """Hàm sắp xếp Merge Sort."""
  if len(a) <= 1:
    return a
  mid = len(a) // 2
  left = merge_sort(a[:mid])
  right = merge_sort(a[mid:])
  return merge(left, right)
