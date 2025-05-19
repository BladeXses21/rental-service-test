fetch('http://backend:8000/api/v1/apartments/')
  .then(res => res.json())
  .then(data => console.log('✅ УСПІХ: Дані з API:', data))
  .catch(err => console.error('❌ ПОМИЛКА API:', err));
